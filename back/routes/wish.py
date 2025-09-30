from flask import Blueprint, jsonify
from db.database import get_db_connection

wish_bp = Blueprint('wish', __name__)

@wish_bp.route("/wish/<int:user_id>", methods=["GET"])
def wish_list(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT w.id as wish_id, p.id as product_id, p.name, p.description, p.price, p.stock
                FROM wish_list w
                JOIN products p ON w.product_id = p.id
                WHERE w.user_id=%s
            """, (user_id,))
            wishes = cursor.fetchall()  # déjà des dicts
    finally:
        conn.close()
    
    return jsonify(wishes)

@wish_bp.route("/add-wish/<int:user_id>/<int:product_id>", methods=["POST"])
def add_to_wishList(user_id, product_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO wish_list (user_id, product_id) VALUES (%s, %s)",
                (user_id, product_id)
            )
        conn.commit()
    finally:
        conn.close()
    
    return jsonify({"message": "Product added to wish_list successfully!"}), 201

@wish_bp.route("/delete-wish/<int:id>", methods=["DELETE"])
def delete_to_wishList(id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM wish_list WHERE id=%s", (id,))
        conn.commit()
    finally:
        conn.close()
    
    return jsonify({"message": "Product deleted successfully from wish_list!"}), 200