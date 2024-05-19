from client_server_app.server.firebase_db import FirebaseDB


def clean_email_filter(username):
    # Remove all non-alphanumeric characters using filter() and join()
    return ''.join(filter(lambda char: char.isalnum(), username))


class Db:
    def __init__(self):
        self.db = FirebaseDB()

    def get_users(self):
        return self.db.get_users() or {}

    def authenticate_user(self, username, password):
        users = self.get_users()
        key = clean_email_filter(username)
        return key in users and users[key]['password'] == password

    def add_user(self, username, password):
        users = self.get_users()
        key = clean_email_filter(username)
        if key in users:
            return False
        self.db.add_user(key, username, password)
        return True

    def add_user_token(self, username, token):
        users = self.get_users()
        key = clean_email_filter(username)
        if key not in users:
            return False
        self.db.add_user_token(key, username, token)
        return True

    def get_user_token(self, username):
        users = self.get_users()
        key = clean_email_filter(username)
        return key in users and users[key]['token']

    def add_order(self, username, order):
        users = self.get_users()
        key = clean_email_filter(username)
        if key not in users:
            return False
        self.db.add_order(key, order)
        return True
