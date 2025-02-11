from flask import jsonify

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
