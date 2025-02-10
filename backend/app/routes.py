import jwt
import datetime
from flask import Blueprint, request, jsonify,  make_response
from app.models import create_user, find_user_by_email
from app.utils import is_valid_email, is_valid_password, create_response, map_category_name
from app import mongo, bcrypt
import requests
from bson import ObjectId

SECRET_KEY = "your-secret-key"  


main = Blueprint('main', __name__)


@main.route('/auth-check', methods=['GET'])
def checkAuth():
    token = request.cookies.get('access_token')

    if not token:
        return jsonify({"error": "Token is missing"}), 401
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        emailId = payload.get('emailId')
        if not emailId:
            return create_response("Email ID is missing in token", 400)
        user = find_user_by_email(emailId)

        if not user:
            return create_response("User not found", 404)
        
        user_data = {key: str(value) if isinstance(value, ObjectId) else value for key, value in user.items()}

        return create_response("User Authorized", 200, user_data)

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

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

    # Generate JWT token
    payload = {
        'emailId': str(user['emailId']),  # Include user emailId in the payload
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token expires in 24 hour
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # Set token in an HTTP-only cookie
    response = make_response(create_response("Login successful", 200, {"role": user["role"]}))
    response.set_cookie(
        key='access_token',
        value=token,
        httponly=True,  # Prevents JavaScript from accessing the cookie
        secure=False,  # ❗ Set this to False for development (must be True for HTTPS in production)
        samesite="Lax",  # Ensures the cookie is sent with same-site requests
        max_age=60 * 60 * 24  # 1 day expiry
    )
    
    return response



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
    # Get token from cookies
    token = request.cookies.get('access_token')

    if not token:
        return jsonify({"error": "Token is missing"}), 401

    try:
        # Decode the token to verify its validity
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        # You can use the user_id from the payload for further processing if needed
        emailId = payload['emailId']

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

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