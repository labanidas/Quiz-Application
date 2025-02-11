from flask import Blueprint
from app.controllers.quiz_controller import fetch_questions
from app.middleware.auth_middleware import token_required

quiz_bp = Blueprint('quiz', __name__)

quiz_bp.route('/fetch-questions', methods=['POST'])(token_required(fetch_questions))
