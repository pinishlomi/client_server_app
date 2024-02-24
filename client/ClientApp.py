import json
import tkinter as tk
from tkinter import messagebox

from client_server_app.client.ServerConnection import ServerConnection
from client_server_app.client.screens.Callback import Callback
from client_server_app.client.screens.LandingPage import LandingPage
from client_server_app.client.screens.Login import Login
from client_server_app.client.screens.Register import Register
from client_server_app.constants import WIDTH, HEIGHT, TITLE
from client_server_app.private_data import HOST, PORT, SECRET_KEY
# from client_server_app.assets.images import sign_up.png


class ClientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.callback = None
        self.server_address = (HOST, PORT)
        self.title(TITLE)
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.current_screen = None
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.server_connection = ServerConnection(HOST, PORT, SECRET_KEY)

    def on_close(self):
        if isinstance(self.current_screen, LandingPage):
            print('sdvds')
            self.destroy()
        else:
            self.show_app()

    def show_app(self):
        self.callback = Callback(self.callback_func)
        self.current_screen = LandingPage(self.callback)
        self.mainloop()

    def callback_func(self):
        print(self.callback)
        if self.callback.type == 'sign_in':
            self.destroy_current()
            self.current_screen = Login(self.callback)

        elif self.callback.type == 'sign_up':
            self.destroy_current()
            self.current_screen = Register(self.callback)

        elif self.callback.type == 'login':
            response = self.login()
            if response['status'] == 'success':
                messagebox.showinfo("Login Successful", response['message'])
                # Optionally, you can switch to another screen here
            else:
                messagebox.showerror("Login Failed", response['message'])
        elif self.callback.type == 'register':
            response = self.join_now()
            if response['status'] == 'success':
                messagebox.showinfo("Login Successful", response['message'])
                # Optionally, you can switch to another screen here
            else:
                messagebox.showerror("Login Failed", response['message'])

    def login(self):
        print(self.callback)
        username = self.callback.data['username']
        password = self.callback.data['password']
        data = {'data': {'type': 'login', 'username': username, 'password': password}}
        data['digest'] = self.server_connection.authenticate(json.dumps(data['data']))
        return self.server_connection.send_data(data)

    def join_now(self):
        print(self.callback)
        username = self.callback.data['username']
        password = self.callback.data['password']
        data = {'data': {'type': 'register', 'username': username, 'password': password}}
        data['digest'] = self.server_connection.authenticate(json.dumps(data['data']))
        return self.server_connection.send_data(data)

    def destroy_current(self):
        if self.current_screen:
            self.current_screen.destroy()


if __name__ == '__main__':
    ClientApp().show_app()
