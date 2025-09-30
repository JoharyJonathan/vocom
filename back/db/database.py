# import sqlite3
# import os

# DB_NAME = "db/database.sqlite"

# # Fonction pour créer la connexion
# def get_db_connection():
#     conn = sqlite3.connect(DB_NAME)
#     conn.row_factory = sqlite3.Row  # Pour accéder aux colonnes par nom
#     return conn

# # Fonction d'initialisation de la base
# def init_db():
#     conn = get_db_connection()

#     conn.commit()
#     conn.close()

from dotenv import load_dotenv
import pymysql
import os

load_dotenv()

# Paramètres de connexion MySQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": False
}

# Fonction pour créer la connexion
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# Fonction d'initialisation de la base
def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
        conn.commit()
    finally:
        conn.close()