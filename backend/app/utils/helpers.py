from datetime import datetime

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

    return categories.get(category_name, None)
