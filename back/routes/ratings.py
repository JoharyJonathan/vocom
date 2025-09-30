from flask import Blueprint, jsonify, request
from db.database import get_db_connection
import pymysql.err

rating_bp = Blueprint('rating', __name__)

@rating_bp.route("/add-rating/<int:user_id>/<int:product_id>", methods=["POST"])
def add_rating(user_id, product_id):
    data = request.get_json()
    rating = data.get("rating")
    comment = data.get("comment", "")

    if not rating or not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO ratings (user_id, product_id, rating, comment) VALUES (%s, %s, %s, %s)",
                    (user_id, product_id, rating, comment)
                )
            except pymysql.err.IntegrityError:
                return jsonify({"error": "You have already rated this product"}), 409
        conn.commit()
    finally:
        conn.close()

    return jsonify({"message": "Rating added successfully!"}), 201