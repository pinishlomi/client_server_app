import hmac
import hashlib
import jwt
from datetime import datetime, timedelta, UTC

from client_server_app.constants import TOKEN_EXPIRATION_TIME
from client_server_app.private_data import SECRET_KEY
from client_server_app.server.Db import Db


def generate_token(username):
    expiration_time = datetime.now(UTC) + timedelta(minutes=TOKEN_EXPIRATION_TIME)
    payload = {
        'username': username,
        'exp': expiration_time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def authenticate(data, client_digest):
    # credential = {'username': username, 'password': password}
    # data_json = json.dumps(credential).encode()
    # data['data'] = credential
    # digest = hmac.new(b'your_secret_key', data_json, hashlib.sha256).hexdigest()

    server_digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()
    print('data: ', data)
    print('server_digest: ', server_digest)
    print('client_digest: ', client_digest)
    return hmac.compare_digest(server_digest, client_digest)


def authenticate_user(username, password):
    db = Db()
    return db.authenticate_user(username, password)
