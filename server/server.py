import socket
import json

from client_server_app.private_data import SECRET_KEY, HOST, PORT
from client_server_app.server.auth import Auth


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
                data = self.__conn.recv(1024)
                if not data:
                    break
                data = json.loads(data.decode())
                client_data = json.dumps(data['data']).encode()
                print('get request: ', data)
                action = data['data']['type']
                if action == 'login':
                    if self.__auth.login_authenticate(client_data, data['digest']):
                        username = data['data']['username']
                        token = self.__auth.generate_token(username)
                        self.__auth.add_user_token(username, token)
                        #  TODO remove this
                        # order = {
                        #     'date' : '24032024',
                        #     'view': 'pool',
                        #     'children':4
                        # }
                        # self.__auth.add_order(username, order)
                        response = {'status': 'success', 'token': token,
                                    'message': 'Data received and authenticated. you '
                                               'are logged in'}
                    else:
                        response = {'status': 'failed', 'message': 'Data received but not authenticated'}
                elif action == 'register':
                    if self.__auth.register_authenticate(client_data, data['digest']):
                        username = data['data']['username']
                        token = self.__auth.generate_token(username)
                        response = {'status': 'success', 'token': token,
                                    'message': 'Data received and authenticated. you '
                                               'are logged in'}
                    else:
                        response = {'status': 'failed', 'message': 'Data received but not authenticated'}
                elif action == 'order':
                    verify = self.__auth.verify_request(data)
                    if verify['status'] == 'success':
                        username = data['data']['username']
                        res = self.__auth.add_order(username, data['order'])
                        print('res order', res)

                        # TODO update db with order details
                        response = {'status': 'success', 'message': 'Server got your message...'}
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
