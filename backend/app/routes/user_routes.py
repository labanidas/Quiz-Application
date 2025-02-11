from flask import Blueprint
from app.controllers.user_controller import test_mongo
from app.middleware.auth_middleware import token_required

user_bp = Blueprint('user', __name__)

user_bp.route('/test-mongo', methods=['GET'])(test_mongo)
