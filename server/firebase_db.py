import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from utils.constants import FIREBASE_CONFIG

"""
Entry claim: None
Exit claim: connects the DB class to realtime database in firebase. 
"""

class FirebaseDB:

    """
    Entry claim: None
    Exit claim: creates connection to firebase.
    """

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

    """
    Entry claim: None
    Exit claim: get user from DB
    """

    def get_users(self):
        try:
            db_users = self.db.child('users')
            users = db_users.get('users')
            return users[0]
        except Exception as e:
            print("Error trying to get users:", e)

    """
    Entry claim: gets key, username and password. 
    Exit claim: add user from db
    """

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


    """
    Entry claim: gets key, username and token. 
    Exit claim: adds user token to the user in firebase. 
    """
    def add_user_token(self, key, username, token):
        try:
            user_ref = self.db.child('users').child(key)
            user_ref.update({
                'token': token
            })
            print(f"User '{username}' update token successfully to the database.")
        except Exception as e:
            print(f"Error adding user '{username}' token: {e}")

    """
    Entry claim: gets key and order details.  
    Exit claim: adds user order to the firebase. 
    """
    def add_order(self, key, order_details):
        try:
            date = order_details['start_date']
            order_ref = self.db.child('orders').child(key).child(date)
            order_ref.set(order_details)
            print(f"User order added successfully to the database.")
        except Exception as e:
            print(f"Error adding order: {e}")
