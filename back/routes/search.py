from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from db.database import get_db_connection
import os
import requests
import re
import pymysql.cursors

load_dotenv()

search_bp = Blueprint('searchs', __name__)

# Search with gemini api
@search_bp.route("/voice_search", methods=["POST"])
def voice_search():
    audio_file = request.files['file']
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    response = requests.post(
        "https://api.gemini.com/v1/speech-to-text",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"file": audio_file}
    )
    transcript = response.json().get("text", "")
    
    results = search_products_in_db(transcript)
    
    return jsonify(results)

def search_products_in_db(query):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT * FROM products
                WHERE name LIKE %s OR description LIKE %s
            """
            
            search_term = f"%{query}%"
            cursor.execute(sql, (search_term, search_term))
            products = cursor.fetchall()
    finally:
        conn.close()
    
    return products

@search_bp.route("/search", methods=["GET"])
def search_products():
    raw_query = request.args.get("query", "") or ""
    # enlever ponctuation (conserve lettres accentuées, chiffres, espaces et tiret)
    normalized = re.sub(r"[^\w\sÀ-ÖØ-öø-ÿ-]", "", raw_query).strip().lower()

    if not normalized:
        return jsonify([])

    conn = get_db_connection()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT id, name, description, price, stock
                FROM products
                WHERE LOWER(name) LIKE %s OR LOWER(description) LIKE %s
            """
            search_term = f"%{normalized}%"
            cursor.execute(sql, (search_term, search_term))
            results = cursor.fetchall()
    finally:
        conn.close()

    return jsonify(results)