import jwt
from flask import request, jsonify
from functools import wraps
from app.models.user_model import find_user_by_email
from config import Config


SECRET_KEY = Config.SECRET_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('access_token')

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            emailId = payload.get('emailId')
            if not emailId:
                return jsonify({"error": "Invalid token"}), 401

            user = find_user_by_email(emailId)
            if not user:
                return jsonify({"error": "User not found"}), 404

            return f(user, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

    return decorated
