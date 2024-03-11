# DB.py
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/SalonDB')
        self.db = self.client['SalonDB']
        self.users_collection = self.db['users']

    def insert_user(self, name, address, email, password):
        # Hash the password before inserting it into the MongoDB collection
        hashed_password = generate_password_hash(password, method='sha256')
        self.users_collection.insert_one({
            'name': name,
            'address': address,
            'email': email,
            'password': hashed_password
        })

    def find_user(self, email, password):
        # Find a user by username in the MongoDB collection
        user = self.users_collection.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            return user
        return None
