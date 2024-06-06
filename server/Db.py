from firebase_db import FirebaseDB

"""
Entry claim: get username
Exit claim: filters the username by 
Removing all non-alphanumeric characters using filter() and join()
"""

def clean_email_filter(username):
    # Remove all non-alphanumeric characters using filter() and join()
    return ''.join(filter(lambda char: char.isalnum(), username))


"""
Entry claim: None 
Exit claim: interface between server and actual db. in my case its firebase db. 
"""
class Db:
    """
    Entry claim: None
    Exit claim: creates object of firebaseDB
    """
    def __init__(self):
        self.db = FirebaseDB()

    """
    Entry claim: None
    Exit claim: get user by using firebase db. 
    """
    def get_users(self):
        return self.db.get_users() or {}

    """
    Entry claim: gets username and password 
    Exit claim: returns true if the user in db 
    and the user password in db equal to the password the user wrote when login. 
    """
    def authenticate_user(self, username, password):
        users = self.get_users()
        key = clean_email_filter(username)
        return key in users and users[key]['password'] == password

    """
    Entry claim: get username and password 
    Exit claim: checks if the user in the users 
    if no returns false else return true. 
    """
    def add_user(self, username, password):
        users = self.get_users()
        key = clean_email_filter(username)
        if key in users:
            return False
        self.db.add_user(key, username, password)
        return True

    """
    Entry claim: gets username and token
    Exit claim: checks if the user in the users 
    if no returns false else adds the token to the user in the db and return true. 
    """
    def add_user_token(self, username, token):
        users = self.get_users()
        key = clean_email_filter(username)
        if key not in users:
            return False
        self.db.add_user_token(key, username, token)
        return True

    """
    Entry claim: gets username
    Exit claim: return the token of the user
    """
    def get_user_token(self, username):
        users = self.get_users()
        key = clean_email_filter(username)
        return key in users and users[key]['token']

    """
    Entry claim: gets username and order
    Exit claim: return false if the username not in db. 
    else, adds the order to db by using firebaseDB class and return true. 
    """
    def add_order(self, username, order):
        users = self.get_users()
        key = clean_email_filter(username)
        if key not in users:
            return False
        self.db.add_order(key, order)
        return True
