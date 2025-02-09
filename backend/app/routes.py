from flask import Blueprint, request
from app.models import create_user, find_user_by_email
from app.utils import is_valid_email, is_valid_password, create_response
from app import mongo

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return create_response("Welcome to the Quiz App Backend!")

@main.route('/register', methods=['POST'])
def register():
    data = request.json

    # Validate Email
    if not is_valid_email(data['email']):
        return create_response("Invalid email format", 400)

    # Validate Password
    if not is_valid_password(data['password']):
        return create_response(
            "Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, and a digit.",
            400,
        )

    # Check if user already exists
    if find_user_by_email(data['email']):
        return create_response("User already exists", 400)

    # Set the role (default to 'user' if not provided)
    role = data.get('role', 'user').lower()

    # Ensure the role is valid (either 'user' or 'admin')
    if role not in ['user', 'admin']:
        return create_response("Invalid role. Allowed values are 'user' or 'admin'.", 400)

    # Create the user
    create_user(data['email'], data['password'], role)
    return create_response("User created successfully", 201)

@main.route('/login', methods=['POST'])
def login():
    data = request.json

    # Check if user exists
    user = find_user_by_email(data['email'])
    if not user or not bcrypt.check_password_hash(user['password'], data['password']):
        return create_response("Invalid email or password", 401)

    return create_response("Login successful", 200, {"role": user["role"]})


@main.route('/test-mongo')
def test_mongo():
    try:
        # Test if MongoDB connection is working
        collections = mongo.db.list_collection_names()
        return {"message": "MongoDB connection successful", "collections": collections}, 200
    except Exception as e:
        return {"error": str(e)}, 500
