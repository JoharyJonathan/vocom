from flask import Blueprint, jsonify, request
from db.database import get_db_connection

cart_bp = Blueprint('cart', __name__)

@cart_bp.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT c.id as cart_id, p.id as product_id, p.name, p.description, p.price, p.stock
                FROM cart c
                JOIN products p ON c.product_id = p.id
                WHERE c.user_id = %s
            """, (user_id,))
            cart = cursor.fetchall()
    finally:
        conn.close()
    
    return jsonify(cart)

@cart_bp.route("/add-cart/<int:user_id>/<int:product_id>", methods=["POST"])
def add_to_cart(user_id, product_id):
    data = request.get_json()
    quantity = data.get("quantity", 1)  # valeur par défaut = 1 si non spécifiée

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (user_id, product_id, quantity)
            )
        conn.commit()
    finally:
        conn.close()
    
    return jsonify({"message": "Product added to cart successfully!"}), 201

@cart_bp.route("/remove-cart/<int:id>", methods=["DELETE"])
def remove_from_cart(id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM cart WHERE id=%s", (id,))
        conn.commit()
    finally:
        conn.close()
    
    return jsonify({"message": "Remove product from cart successfully!"})