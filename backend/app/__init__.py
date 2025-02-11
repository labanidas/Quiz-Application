from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from config import Config

# Initialize extensions
mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    mongo.init_app(app)
    bcrypt.init_app(app)
    CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

    # Register Blueprints (Routes)
    from app.routes.auth_routes import auth_bp
    from app.routes.quiz_routes import quiz_bp
    from app.routes.user_routes import user_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
    app.register_blueprint(user_bp, url_prefix='/api/user')

    return app
