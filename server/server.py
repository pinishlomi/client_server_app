import socket
import hmac
import hashlib
import json

from hotel.private_data import SECRET_KEY, HOST, PORT


def authenticate(data, client_digest):
    # credential = {'username': username, 'password': password}
    # data_json = json.dumps(credential).encode()
    # data['data'] = credential
    # digest = hmac.new(b'your_secret_key', data_json, hashlib.sha256).hexdigest()

    server_digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()
    print('data: ' , data)
    print('server_digest: ' , server_digest)
    print('client_digest: ', client_digest)
    return hmac.compare_digest(server_digest, client_digest)


def handle_client_connection(conn, addr):
    print(f"Connection from {addr} has been established.")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = json.loads(data.decode())
        client_data = json.dumps(data['data']).encode()
        print('get request: ', data)
        if authenticate(client_data, data['digest']):
            # Handle authenticated data
            # Save data to database or process accordingly
            request_type = data['data']['type']
            if request_type == 'login':
                response = {'status': 'success', 'message': 'Data received and authenticated. you are logged in'}
            elif request_type == 'register':
                response = {'status': 'success', 'message': 'Data received and authenticated. you are register'}
            else:
                response = {'status': 'success',
                            'message': 'Data received and authenticated, but request type is unknown...'}

        else:
            response = {'status': 'error', 'message': 'Authentication failed.'}
        conn.send(json.dumps(response).encode())
    conn.close()


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        handle_client_connection(conn, addr)


if __name__ == "__main__":
    start_server(HOST, PORT)
