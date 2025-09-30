from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db.database import init_db
import os
from dotenv import load_dotenv
from routes.products import product_bp
from routes.users import auth_bp
from routes.wish import wish_bp
from routes.cart import cart_bp
from routes.orders import order_bp
from routes.ratings import rating_bp
from routes.search import search_bp

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
CORS(app, origins=["http://localhost:5173"])

jwt = JWTManager(app)
init_db()

app.register_blueprint(product_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(wish_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(order_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)