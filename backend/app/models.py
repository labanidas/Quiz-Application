from datetime import datetime, timezone
from app import mongo, bcrypt
from app.utils import format_date

def create_user(email, password, role="user"):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = {
        "emailId": email,
        "password": hashed_password,
        "timestamps": format_date(datetime.now(timezone.utc),),
        "role": role
    }
    mongo.db.users.insert_one(user)

def find_user_by_email(email):
    return mongo.db.users.find_one({"emailId": email})

