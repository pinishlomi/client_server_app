class Db:
    def __init__(self):
        # Simulated user database (replace with actual database)
        self.__users = {
            'u1': {'password': '16365877c300ad49438bb66c5dfc162ae65812a43df54345f0d04728a701562a', 'token': ''},
            'u2': {'password': 'p2', 'token': ''}
        }

    def authenticate_user(self, username, password):
        return username in self.__users and self.__users[username]['password'] == password

    def add_user(self, username, password):
        if username in self.__users:
            return False
        self.__users[username] = password
        return True

    def add_user_token(self, username, token):
        if username not in self.__users.keys():
            return False
        self.__users[username]['token'] = token
        return True

    def get_user_token(self, username):
        return username in self.__users.keys() and self.__users[username]['token']

