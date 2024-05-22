import json
import socket

from utils.private_data import HOST, PORT
from auth import Auth


class Server:
    def __init__(self):
        self.__addr = None
        self.__conn = None
        self.__auth = Auth()
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start_server(HOST, PORT)

    def start_server(self, host, port):
        self.__server_socket.bind((host, port))
        self.__server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            self.__conn, self.__addr = self.__server_socket.accept()
            self.handle_client_connection()

    def handle_client_connection(self):
        print(f"Connection from {self.__addr} has been established.")
        try:
            while True:
                request_data = self.__conn.recv(1024)
                if not request_data:
                    break
                request_data = json.loads(request_data.decode())
                client_data = json.dumps(request_data['data']).encode()
                action = request_data['data']['type']
                if action == 'login':
                    if self.__auth.login_authenticate(client_data, request_data['digest']):
                        username = request_data['data']['username']
                        token = self.__auth.generate_token(username)
                        res = self.__auth.add_user_token(username, token)
                        if res:
                            response = {'status': 'success', 'token': token,
                                        'message': 'Data received and authenticated. you '
                                                   'are logged in'}
                        else:
                            response = {'status': 'failed',
                                        'message': 'Somthing went wrong, server failed to add you to users'}
                    else:
                        response = {'status': 'failed', 'message': 'Data received but not authenticated'}
                elif action == 'register':
                    if self.__auth.register_authenticate(client_data, request_data['digest']):
                        username = request_data['data']['username']
                        token = self.__auth.generate_token(username)
                        res = self.__auth.add_user_token(username, token)
                        if res:
                            response = {'status': 'success', 'token': token,
                                        'message': 'Data received and authenticated. you '
                                                   'are logged in'}
                        else:
                            response = {'status': 'failed',
                                        'message': 'Somthing went wrong, server failed to add you to users'}
                    else:
                        response = {'status': 'failed', 'message': 'Data received but not authenticated'}
                elif action == 'order':
                    verify = self.__auth.verify_request(request_data)
                    if verify['status'] == 'success':
                        username = request_data['data']['username']
                        res = self.__auth.add_order(username, request_data['order'])
                        if res:
                            response = {'status': 'success', 'message': 'order added'}
                        else:
                            response = {'status': 'failed',
                                        'message': 'Somthing went wrong, server failed to add order'}
                    else:
                        response = {'status': 'failed', 'message': verify['message']}
                else:
                    response = {'status': 'failed', 'message': 'Data received but request type is unknown...'}
                self.__conn.send(json.dumps(response).encode())
        except Exception as e:
            print(e)
        finally:
            self.__conn.close()


if __name__ == "__main__":
    Server()
