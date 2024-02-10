import tkinter as tk
from hotel.client.screens import Callback


class Login(tk.Frame):
    def __init__(self, callback: Callback):
        super().__init__()
        self.callback = callback
        self.password_entry = None
        self.username_entry = None
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")
        tk.Label(self, text="Login", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="Username:").grid(row=1, column=0, sticky="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, pady=5)
        tk.Label(self, text="Password:").grid(row=2, column=0, sticky="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        self.callback.type = 'login'
        self.callback.data = {'username': self.username_entry.get(), 'password': self.password_entry.get()}
        self.callback.function()
