from flask_cors import CORS  # Import CORS from flask_cors
from app import create_app
import os

app = create_app()

# Enable CORS for the app
# CORS(app, supports_credentials=True, origins=["http://localhost:5173"]) 

CORS(app, supports_credentials=True, origins=[
    "http://localhost:5173",  # For local development
    "https://your-frontend-domain.com"  # Add your deployed frontend URL
])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get port from Railway
    app.run(host="0.0.0.0", port=port)
