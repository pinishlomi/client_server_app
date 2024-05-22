import hmac
import hashlib
import jwt
import json
from datetime import datetime, timedelta, UTC

from utils.constants import TOKEN_EXPIRATION_TIME
from utils.private_data import SECRET_KEY
from Db import Db


class Auth:
    def __init__(self):
        self.__db = Db()

    def compare_digest(self, data, client_digest):
        server_digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()
        return hmac.compare_digest(server_digest, client_digest)

    def generate_token(self, username):
        expiration_time = datetime.now(UTC) + timedelta(minutes=TOKEN_EXPIRATION_TIME)
        payload = {
            'username': username,
            'exp': expiration_time
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    def __verify_token(self, token):
        verify = {'status': 'failed'}
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            verify['status'] = 'success'
        except jwt.ExpiredSignatureError:
            verify['message'] = 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            verify['message'] = 'Invalid token. Please log in again.'
        finally:
            return verify

    def login_authenticate(self, data, client_digest):
        if self.compare_digest(data, client_digest):
            client_data = json.loads(data.decode())
            hmac_password = hmac.new(SECRET_KEY, json.dumps(client_data['password']).encode(),
                                     hashlib.sha256).hexdigest()
            return self.__db.authenticate_user(client_data['username'], hmac_password)
        return False

    def register_authenticate(self, data, client_digest):
        if self.compare_digest(data, client_digest):
            client_data = json.loads(data.decode())
            hmac_password = hmac.new(SECRET_KEY, json.dumps(client_data['password']).encode(),
                                     hashlib.sha256).hexdigest()
            return self.__db.add_user(client_data['username'], hmac_password)
        return False

    def add_user_token(self, username, token):
        return self.__db.add_user_token(username, token)

    def verify_request(self, data):
        db_token = self.__db.get_user_token(data['data']['username'])
        client_token = data['data']['token']
        if db_token != client_token:
            return {'status': 'failed'}
        return self.__verify_token(client_token)

    def add_order(self, username, order):
        return self.__db.add_order(username, order)
