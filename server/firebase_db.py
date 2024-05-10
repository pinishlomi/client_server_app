import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from client_server_app.constants import FIREBASE_CONFIG


class FirebaseDB:
    def __init__(self):
        # Path to your Service Account key (JSON file)
        self.cred_obj = credentials.Certificate('private_key.json')
        # Firebase database URL
        self.firebase_url = FIREBASE_CONFIG['databaseURL']
        # Initialize the app with the credentials and database URL
        self.app = firebase_admin.initialize_app(self.cred_obj, {
            'databaseURL': self.firebase_url
        })
        # Reference to the root of your database
        self.db = db.reference()

    def connect_db(self):
        # Connect to Firebase database
        try:
            data = self.db.get()
            print("Successfully connected to Firebase database.")
            print("Data from Firebase:", data)
        except Exception as e:
            print("Error connecting to Firebase database:", e)

    def get_users(self):
        try:
            db_users = self.db.child('users')
            users = db_users.get('users')
            return users[0]
        except Exception as e:
            print("Error trying to get users:", e)

    def add_user(self, key, username, password):
        try:
            user_ref = self.db.child('users').child(key)
            user_ref.set({
                'username': username,
                'password': password
            })
            print(f"User '{username}' added successfully to the database.")
        except Exception as e:
            print(f"Error adding user '{username}': {e}")

    def add_user_token(self, key, username, token):
        try:
            user_ref = self.db.child('users').child(key)
            user_ref.update({
                'token': token
            })
            print(f"User '{username}' update token successfully to the database.")
        except Exception as e:
            print(f"Error adding user '{username}' token: {e}")

    def add_order(self, key, order_details):
        try:
            date = order_details['start_date']
            order_ref = self.db.child('orders').child(key).child(date)
            order_ref.set(order_details)
            print(f"User order added successfully to the database.")
        except Exception as e:
            print(f"Error adding order: {e}")
