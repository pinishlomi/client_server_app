class Db:
    def __init__(self):
        # Simulated user database (replace with actual database)
        self.__users = {
            'user1': {'password': 'password1', 'role': 'admin'},
            'user2': {'password': 'password2', 'role': 'user'}
        }

    def authenticate_user(self, username, password):
        return username in self.__users and self.__users[username]['password'] == password
