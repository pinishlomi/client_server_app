import hashlib
import hmac
import json
import socket

"""
Entry claim: None
Exit claim: send data to the server 
with / without authentication.  
"""
class ServerConnection:

    """
    Entry claim: gets host, port, secret key
    Exit claim: sets the host, port and the secret key in class,
    same as the host, port and secret key in entry claim.
    """

    def __init__(self, host, port, secret_key):
        self.host = host
        self.port = port
        self.secret_key = secret_key

    """
    Entry claim: gets data
    Exit claim:  returns the digest. the digest in encryption with hash function 
    that combines the secret key and the data. 
    """
    def authenticate(self, data):
        digest = hmac.new(self.secret_key, data.encode(), hashlib.sha256).hexdigest()
        return digest

    """
    Entry claim: gets data
    Exit claim: returns the response from the server. and sends the data to the server.  
    """

    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.host, self.port))
                s.sendall(json.dumps(data).encode())
                response = s.recv(1024).decode()
                return json.loads(response)
            except ConnectionError:
                return {'status': 'error', 'message': 'Failed to connect to the server.'}
