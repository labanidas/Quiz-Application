from flask_cors import CORS  # Import CORS from flask_cors
from app import create_app

app = create_app()

# Enable CORS for the app
CORS(app, supports_credentials=True, origins=["http://localhost:5173"]) 

if __name__ == '__main__':
    app.run(debug=True)
