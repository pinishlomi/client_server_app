import json
import tkinter as tk
from tkinter import messagebox

from client_server_app.client.ServerConnection import ServerConnection
from client_server_app.client.screens.Callback import Callback
from client_server_app.client.screens.LandingPage import LandingPage
from client_server_app.client.screens.Login import Login
from client_server_app.client.screens.MessagePage import MessagePage
from client_server_app.client.screens.Register import Register
from client_server_app.constants import WIDTH, HEIGHT, TITLE
from client_server_app.private_data import HOST, PORT, SECRET_KEY


class ClientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__callback = None
        self.__server_address = (HOST, PORT)
        self.title(TITLE)
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        print(f'main : {self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.__current_screen = None
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.__server_connection = ServerConnection(HOST, PORT, SECRET_KEY)
        self.__token = None
        self.__username = None
        self.__user_authenticate = False

    def clear_all_items(self):
        for widget in self.pack_slaves():
            widget.pack_forget()

    def on_close(self):
        if isinstance(self.__current_screen, LandingPage):
            self.destroy()
        if isinstance(self.__current_screen, MessagePage):
            self.__callback.data = {'user_authenticate': self.__user_authenticate}
            self.__current_screen = LandingPage(self.__callback)
        else:
            self.show_app()

    def show_app(self):
        self.__callback = Callback(self.callback_func)
        self.clear_all_items()
        self.__current_screen = LandingPage(self, self.__callback)
        # if self.__user_authenticate:
        #     self.__current_screen = MessagePage(self.__callback)
        # else:
        #     self.__current_screen = LandingPage(self, self.__callback)
        self.mainloop()

    def callback_func(self):
        print(self.__callback)
        if self.__callback.type == 'sign_in':
            self.destroy_current()
            self.clear_all_items()
            self.__current_screen = Login(self, self.__callback)

        elif self.__callback.type == 'sign_up':
            self.destroy_current()
            self.clear_all_items()
            self.__current_screen = Register(self, self.__callback)

        elif self.__callback.type == 'login':
            response = self.login()
            if response['status'] == 'success':
                self.__token = response['token']
                self.__username = self.__callback.data['username']
                self.__user_authenticate = True
                # messagebox.showinfo("Login Successful", response['message'])
                self.show_app()
            else:
                messagebox.showerror("Login Failed", response['message'])
        elif self.__callback.type == 'register':
            response = self.join_now()
            if response['status'] == 'success':
                self.__token = response['token']
                self.__username = self.__callback.data['username']
                self.__user_authenticate = True
                # messagebox.showinfo("Login Successful", response['message'])
                self.show_app()
            else:
                messagebox.showerror("Login Failed", response['message'])
        elif self.__callback.type == 'message':
            response = self.send_message()
            if response['status'] == 'success':
                if isinstance(self.__current_screen, MessagePage):
                    self.__current_screen.add_message('Server', response['message'])
            else:
                messagebox.showerror("Send Message Failed", response['message'])
                self.__user_authenticate = False
                self.show_app()

    def login(self):
        username = self.__callback.data['username']
        password = self.__callback.data['password']
        data = {'data': {'type': 'login', 'username': username, 'password': password}}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    def join_now(self):
        username = self.__callback.data['username']
        password = self.__callback.data['password']
        data = {'data': {'type': 'register', 'username': username, 'password': password}}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    def send_message(self):
        data = {'data': {'type': 'message', 'username': self.__username, 'token': self.__token},
                'message': 'Try to send message to server'}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    def destroy_current(self):
        if self.__current_screen:
            self.__current_screen.destroy()


if __name__ == '__main__':
    ClientApp().show_app()
