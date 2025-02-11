import requests
from flask import request, jsonify
from app.utils.helpers import map_category_name

def fetch_questions(user):
    data = request.json

    required_fields = ["amount", "category", "difficulty", "type"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required."}), 400

    category_id = map_category_name(data["category"])
    if category_id is None:
        return jsonify({"error": "Invalid category provided."}), 400

    url = f"https://opentdb.com/api.php?amount={data['amount']}&category={category_id}&difficulty={data['difficulty']}&type={data['type']}"

    try:
        response = requests.get(url)
        response_data = response.json()

        if response_data["response_code"] != 0:
            return jsonify({"error": "Failed to fetch questions from the API."}), 500

        return jsonify({"questions": response_data["results"]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
