import jwt
import datetime
from flask import request, jsonify, make_response
from bson import ObjectId
from app.models.user_model import create_user, find_user_by_email
from app.utils.validation import is_valid_email, is_valid_password
from app.utils.response import create_response
from config import Config
from app import bcrypt


SECRET_KEY = Config.SECRET_KEY


def register():
    """
    Handles user registration.
    """
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return create_response("Email and password are required.", 400)

    email = data['email'].strip().lower()
    password = data['password'].strip()

    if not is_valid_email(email):
        return create_response("Invalid email format", 400)

    if not is_valid_password(password):
        return create_response(
            "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, and a digit.",
            400,
        )

    if find_user_by_email(email):
        return create_response("User already exists", 400)

    role = data.get('role', 'user').strip().lower()
    if role not in ['user', 'admin']:
        return create_response("Invalid role. Allowed values are 'user' or 'admin'.", 400)

    create_user(email, password, role)
    return create_response("User created successfully", 201)

def login():
    """
    Handles user login and JWT token generation.
    """
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return create_response("Email and password are required.", 400)

    email = data['email'].strip().lower()
    password = data['password'].strip()

    user = find_user_by_email(email)
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return create_response("Invalid email or password", 401)

    # Generate JWT token with timezone-aware expiration
    payload = {
        'emailId': email,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    response = make_response(create_response("Login successful", 200, {"role": user["role"]}))
    response.set_cookie(
        key='access_token',
        value=token,
        httponly=True,
        secure=False,  # Change to True in production with HTTPS
        samesite="Lax",
        max_age=60 * 60 * 24  # 1 day expiry
    )
    
    return response

def check_auth(user):
    """
    Checks if the user is authorized.
    """
    if not user:
        return create_response("User not found", 404)

    user_data = {key: str(value) if isinstance(value, ObjectId) else value for key, value in user.items()}
    return create_response("User Authorized", 200, user_data)
