# import sqlite3
# from werkzeug.security import generate_password_hash

# DB_NAME = "database.sqlite"

# def seed_users():
#     users = [
#         ("alice", "alice@example.com", "password123"),
#         ("bob", "bob@example.com", "securepass"),
#         ("charlie", "charlie@example.com", "charliepwd"),
#         ("david", "david@example.com", "mypassword"),
#         ("eve", "eve@example.com", "eve12345"),
#     ]

#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     for username, email, password in users:
#         try:
#             cursor.execute(
#                 "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
#                 (username, email, generate_password_hash(password))
#             )
#         except sqlite3.IntegrityError:
#             print(f"⚠️ User {username} already exists, skipping.")

#     conn.commit()
#     conn.close()
#     print("✅ Users seeded successfully!")

# if __name__ == "__main__":
#     seed_users()

from werkzeug.security import generate_password_hash
from database import get_db_connection

def seed_users():
    users = [
        ("alice", "alice@example.com", "password123"),
        ("bob", "bob@example.com", "securepass"),
        ("charlie", "charlie@example.com", "charliepwd"),
        ("david", "david@example.com", "mypassword"),
        ("eve", "eve@example.com", "eve12345"),
    ]

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            for username, email, password in users:
                try:
                    cursor.execute(
                        """
                        INSERT INTO users (username, email, password_hash) 
                        VALUES (%s, %s, %s)
                        """,
                        (username, email, generate_password_hash(password))
                    )
                except conn.err.ProgrammingError:
                    print(f"⚠️ User {username} already exists, skipping.")
                except Exception as e:
                    print(f"⚠️ Error inserting {username}: {e}")

        conn.commit()
        print("✅ Users seeded successfully!")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_users()