from flask import Blueprint, jsonify, request
from db.database import get_db_connection
import pymysql.err

order_bp = Blueprint("order", __name__)

@order_bp.route("/create-order/<int:user_id>", methods=["POST"])
def create_order(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            # Récupérer les produits du panier
            cursor.execute("""
                SELECT c.product_id, c.quantity, p.price
                FROM cart c
                JOIN products p ON c.product_id = p.id
                WHERE c.user_id=%s
            """, (user_id,))
            cart_items = cursor.fetchall()  # déjà des dicts

            if not cart_items:
                return jsonify({"error": "Cart is empty"}), 400

            # Calculer total
            total = sum(item["quantity"] * float(item["price"]) for item in cart_items)

            # Créer la commande
            cursor.execute(
                "INSERT INTO orders (user_id, status, total) VALUES (%s, %s, %s)",
                (user_id, "pending", total)
            )
            order_id = cursor.lastrowid

            # Ajouter les produits à order_items
            for item in cart_items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                    (order_id, item["product_id"], item["quantity"], item["price"])
                )

            # Vider le panier
            cursor.execute("DELETE FROM cart WHERE user_id=%s", (user_id,))
        conn.commit()

        return jsonify({"message": "Order created successfully", "order_id": order_id, "total": total}), 201

    except pymysql.err.OperationalError as e:
        if "lock" in str(e).lower():
            return jsonify({"error": "Database is locked, please retry"}), 503
        raise
    finally:
        conn.close()