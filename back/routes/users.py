from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from db.database import get_db_connection
import pymysql.err
import datetime

auth_bp = Blueprint("auth", __name__)

# -----------------------------
# Route d'inscription (signup)
# -----------------------------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    password_hash = generate_password_hash(password)

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
                    (username, email, password_hash)
                )
            except pymysql.err.IntegrityError:
                return jsonify({"error": "Username or email already exists"}), 409
        conn.commit()
        return jsonify({"message": "User created successfully"}), 201
    finally:
        conn.close()


# -----------------------------
# Route de connexion (login)
# -----------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cursor.fetchone()
    finally:
        conn.close()

    if user and check_password_hash(user["password_hash"], password):
        expires = datetime.timedelta(hours=1)
        access_token = create_access_token(identity=str(user["id"]), expires_delta=expires)
        return jsonify({
            "message": "Login successful",
            "token": access_token,
            "user": {"id": user["id"], "username": user["username"], "email": user["email"]}
        }), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# -----------------------------
# Exemple de route protégée
# -----------------------------
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, username, email, created_at FROM users WHERE id=%s",
                (current_user_id,)
            )
            user = cursor.fetchone()
    finally:
        conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200