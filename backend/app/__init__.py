from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from config import Config

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    mongo.init_app(app)
    bcrypt.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
