from flask import Blueprint, jsonify, request
from db.database import get_db_connection

product_bp = Blueprint('product', __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
    finally:
        conn.close()

    return jsonify(products)

@product_bp.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
            product = cursor.fetchone()
    finally:
        conn.close()

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)

@product_bp.route("/new-product", methods=["POST"])
def add_product():
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")
    stock = request.form.get("stock")

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)",
                (name, description, price, stock)
            )
        conn.commit()
    finally:
        conn.close()

    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route("/delete-product/<int:id>", methods=["DELETE"])
def delete_product(id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        conn.commit()
    finally:
        conn.close()

    return jsonify({"message": "Product deleted successfully"}), 200

@product_bp.route("/update-product/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE products SET name=%s, description=%s, price=%s, stock=%s WHERE id=%s",
                (name, description, price, stock, id)
            )
        conn.commit()
    finally:
        conn.close()

    return jsonify({"message": "Product updated successfully"}), 200