import json
import tkinter as tk
from tkinter import messagebox

from server_con.ServerConnection import ServerConnection
from utils.Callback import Callback
from screens.LandingPage import LandingPage
from screens.Login import Login
from screens.Order import Order
from screens.Register import Register
from utils.constants import TITLE
from utils.private_data import HOST, PORT, SECRET_KEY


"""
Entry claim: inherit from tk.Tk (Tkinter - UI)
Exit claim: Manage all UI - sets the active screen, response by running the callback function. 
"""
class ClientApp(tk.Tk):
    """
    Entry claim: None
    Exit claim: initialize all the required data, creates server connection and sets the screen size.
    """

    def __init__(self):
        super().__init__()   # run the tk.Tk init
        self.__callback = None
        self.__server_address = (HOST, PORT)
        self.title(TITLE)
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.__current_screen = None
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.__server_connection = ServerConnection(HOST, PORT, SECRET_KEY)
        self.__token = None
        self.__username = None
        self.__user_authenticate = False

    """
    Entry claim: None
    Exit claim:  go over all the existing widgets in the screen and forget them. 
    """
    def clear_all_items(self):
        for widget in self.pack_slaves():
            widget.pack_forget()

    """
    Entry claim: None
    Exit claim: method that listens if user press the close screen
    and jump to the right screen depending the screen the user closes. 
    """
    def on_close(self):
        if (isinstance(self.__current_screen, LandingPage) or
                isinstance(self.__current_screen, Order)):
            self.destroy()
        else:
            self.show_app()

    """
    Entry claim: None
    Exit claim: shows the relevant screen depending user authentication. 
    """
    def show_app(self):
        self.__callback = Callback(self.callback_func)
        self.clear_all_items()
        if self.__user_authenticate:
            self.__current_screen = Order(self, self.__callback)
        else:
            self.__current_screen = LandingPage(self, self.__callback)
        self.mainloop()

    """
    Entry claim: None
    Exit claim:  this function is the main logic of the UI. 
    it controls the actions that triggers from other screens. 
    """

    def callback_func(self):
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
                self.show_app()
            else:
                messagebox.showerror("Login Failed", response['message'])

        elif self.__callback.type == 'register':
            response = self.join_now()
            if response['status'] == 'success':
                self.__token = response['token']
                self.__username = self.__callback.data['username']
                self.__user_authenticate = True
                self.show_app()
            else:
                messagebox.showerror("Login Failed", response['message'])

        elif self.__callback.type == 'order':
            if self.__user_authenticate:
                response = self.send_order()
                if response['status'] == 'success':
                    order_details = self.__callback.data['order']
                    st = f'Start Vacation in:  {order_details["start_date"]} \n'
                    st += f'End Vacation in:  {order_details["end_date"]} \n'
                    st += f'Number of Adults: {order_details["num_adults"]} \n'
                    st += f'Number of Kids: {order_details["num_kids"]} \n'
                    st += f'Number of rooms: {order_details["num_rooms"]} \n'
                    st += f'Number of meals: {order_details["meals"]} \n'
                    messagebox.showinfo("Order Summary", st)
                else:
                    messagebox.showerror("Login Failed, Please try again", response['message'])
                    self.__user_authenticate = False
                    self.show_app()
            else:
                messagebox.showerror("Login Failed, Please try again", "Login expired, You need to login again")
                self.show_app()
        else:
            print('Unknown type')
            self.show_app()

    """
    Entry claim: None
    Exit claim:  returns server connection response. 
    and sets the data to send to the server in dictionary.
    """

    def login(self):
        username = self.__callback.data['username']
        password = self.__callback.data['password']
        data = {'data': {'type': 'login', 'username': username, 'password': password}}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    """
    Entry claim: None
    Exit claim: returns server connection response. 
    and sets the data to send to the server in dictionary. 
    """

    def join_now(self):
        username = self.__callback.data['username']
        password = self.__callback.data['password']
        data = {'data': {'type': 'register', 'username': username, 'password': password}}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    """
    Entry claim: None
    Exit claim: returns server connection response. 
    and sets the data to send to the server in dictionary. 
    """
    def send_order(self):
        order_details = self.__callback.data['order']
        data = {'data': {'type': 'order', 'username': self.__username, 'token': self.__token},
                'order': order_details}
        data['digest'] = self.__server_connection.authenticate(json.dumps(data['data']))
        return self.__server_connection.send_data(data)

    """
    Entry claim: None
    Exit claim: closes the current screen.   
    """
    def destroy_current(self):
        if self.__current_screen:
            self.__current_screen.destroy()


if __name__ == '__main__':
    client = ClientApp()
    client.show_app()
