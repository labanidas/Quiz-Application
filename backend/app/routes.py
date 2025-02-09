from flask import Blueprint, request, jsonify
from app.models import create_user, find_user_by_email
from app.utils import is_valid_email, is_valid_password, create_response, map_category_name
from app import mongo, bcrypt
import requests


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
    

@main.route('/fetch-questions', methods=['POST'])
def fetch_questions():
    # Get data from the frontend (JSON payload)
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input. Please provide data in JSON format."}), 400

    # Validate the required fields
    required_fields = ["amount", "category", "difficulty", "type"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required."}), 400

    # Map category name to category ID
    category_id = map_category_name(data["category"])
    if category_id is None:
        return jsonify({"error": "Invalid category provided."}), 400

    # Build the Open Trivia API URL
    url = f"https://opentdb.com/api.php?amount={data['amount']}&category={category_id}&difficulty={data['difficulty']}&type={data['type']}"

    try:
        # Make a GET request to the Open Trivia API
        response = requests.get(url)
        response_data = response.json()

        # Handle response from the API
        if response_data["response_code"] != 0:
            return jsonify({"error": "Failed to fetch questions from the API."}), 500

        # Return the fetched questions to the user
        return jsonify({"questions": response_data["results"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
