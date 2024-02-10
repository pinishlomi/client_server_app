import hashlib
import hmac
import json
import socket


class ServerConnection:
    def __init__(self, host, port, secret_key):
        self.host = host
        self.port = port
        self.secret_key = secret_key

    def authenticate(self, data):
        digest = hmac.new(self.secret_key, data.encode(), hashlib.sha256).hexdigest()
        return digest

    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                s.sendall(json.dumps(data).encode())
                response = s.recv(1024).decode()
                print('response from server: ', json.loads(response))
                return json.loads(response)
            except ConnectionError:
                return {'status': 'error', 'message': 'Failed to connect to the server.'}
