from flask import jsonify
from app import mongo
from app.utils.response import create_response

def test_mongo():
    """
    Tests MongoDB connection by listing collections.
    """
    try:
        collections = mongo.db.list_collection_names()
        return create_response("MongoDB connection successful", 200, {"collections": collections})
    except Exception as e:
        return create_response(f"MongoDB Error: {str(e)}", 500)
