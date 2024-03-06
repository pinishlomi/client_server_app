import tkinter as tk
from client_server_app.client.screens import Callback


class LandingPage(tk.Frame):
    def __init__(self, callback: Callback):
        super().__init__()
        self.callback = callback
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, text="Landing Page", font=("Helvetica", 26)).grid(row=0, column=0, columnspan=10, pady=10)
        if self.callback.data and self.callback.data.get('user_authenticate', False):
            pass
            # show somthing else
        else:
            sign_in_button = tk.Button(self, text="Sign in", command=self.sign_in)
            sign_in_button.grid(row=3, column=0, columnspan=2, pady=10)
            register_button = tk.Button(self, text="Register", command=self.join_now)
            register_button.grid(row=3, column=3, columnspan=2, pady=10)

    def sign_in(self):
        self.callback.type = 'sign_in'
        self.callback.data = 'Sign in clicked'
        self.callback.function()

    def join_now(self):
        self.callback.type = 'sign_up'
        self.callback.data = 'sign_up clicked'
        self.callback.function()
