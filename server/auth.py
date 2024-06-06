import hmac
import hashlib
import jwt
import json
from datetime import datetime, timedelta, UTC

from utils.constants import TOKEN_EXPIRATION_TIME
from utils.private_data import SECRET_KEY
from Db import Db


"""
Entry claim: None
Exit claim: handle all the authentication processes in the system
"""
class Auth:
    """
    Entry claim: None
    Exit claim:  creates object of the db class.
    """

    def __init__(self):
        self.__db = Db()

    """
    Entry claim: gets data, and the client digest
    Exit claim: return true if the server digest equals to the client digest 
    """
    def compare_digest(self, data, client_digest):
        server_digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()
        return hmac.compare_digest(server_digest, client_digest)

    """
    Entry claim: gets username
    Exit claim: creates and returns a token for the username he got. 
    """
    def generate_token(self, username):
        expiration_time = datetime.now(UTC) + timedelta(minutes=TOKEN_EXPIRATION_TIME)
        payload = {
            'username': username,
            'exp': expiration_time
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    """
    Entry claim: gets token
    Exit claim: return a dictionary for the status of the token. 
    """

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


    """
    Entry claim: gets data and client digest
    Exit claim: return true if the user in db and authenticated.
    else, return false.  
    """
    def login_authenticate(self, data, client_digest):
        if self.compare_digest(data, client_digest):
            client_data = json.loads(data.decode())
            hmac_password = hmac.new(SECRET_KEY, json.dumps(client_data['password']).encode(),
                                     hashlib.sha256).hexdigest()
            return self.__db.authenticate_user(client_data['username'], hmac_password)
        return False


    """
    Entry claim: gets data and client digest
    Exit claim: return true if the user added to db and authenticate. 
    else, return false. 
    """

    def register_authenticate(self, data, client_digest):
        if self.compare_digest(data, client_digest):
            client_data = json.loads(data.decode())
            hmac_password = hmac.new(SECRET_KEY, json.dumps(client_data['password']).encode(),
                                     hashlib.sha256).hexdigest()
            return self.__db.add_user(client_data['username'], hmac_password)
        return False

    """
    Entry claim: gets username and token
    Exit claim: returns true if the token added to the username in db. 
    """

    def add_user_token(self, username, token):
        return self.__db.add_user_token(username, token)

    """
    Entry claim: gets data.
    Exit claim: checks if the user token equal to the db token. 
    and send the status
    """
    def verify_request(self, data):
        db_token = self.__db.get_user_token(data['data']['username'])
        client_token = data['data']['token']
        if db_token != client_token:
            return {'status': 'failed'}
        return self.__verify_token(client_token)

    """
    Entry claim: gets username and order details. 
    Exit claim: return true if the order added to db. else, false.  
    """

    def add_order(self, username, order):
        return self.__db.add_order(username, order)
