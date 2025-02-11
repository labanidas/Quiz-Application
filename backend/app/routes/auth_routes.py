from flask import Blueprint
from app.controllers.auth_controller import register, login, check_auth
from app.middleware.auth_middleware import token_required

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)
# auth_bp.route('/auth-check', methods=['GET'])(check_auth)
auth_bp.route('/auth-check', methods=['GET'])(token_required(check_auth))
