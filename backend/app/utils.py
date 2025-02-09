import re
from flask import jsonify
from datetime import datetime


# Password Validation
def is_valid_password(password):
    """
    Validates a password to check if it meets the criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    """
    if len(password) < 6:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True


# JSON Response Helper
def create_response(message, status=200, data=None):
    """
    Creates a consistent JSON response format.
    """
    response = {
        "message": message,
        "status": status,
    }
    if data:
        response["data"] = data
    return jsonify(response), status


# Email Validation Utility
def is_valid_email(email):
    """
    Validates if an email is in the correct format.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# Date Formatting Utility
def format_date(date):
    """
    Formats a datetime object into a readable string format.
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")


def map_category_name(category_name):
    """
    Map category name from the frontend to the corresponding category ID for the Open Trivia Database API.
    """
    categories = {
        "Any Category": 0,
        "General Knowledge": 9,
        "Geography": 22,
        "Science: Computers": 18,
        # Add more categories as needed
    }

    return categories.get(category_name)

