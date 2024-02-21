import tkinter as tk
from client_server_app.client.screens import Callback
from PIL import Image, ImageTk


class Register(tk.Frame):
    def __init__(self, callback: Callback):
        super().__init__()
        self.callback = callback
        self.password_entry = None
        self.username_entry = None
        self.show()

    def show(self):
        # Load background image
        # background_image = Image.open("sign_up.png")  # Replace with your image file path
        # background_image = background_image.resize((600, 600))
        # self.background_photo = ImageTk.PhotoImage(background_image)
        #
        # # Create a Canvas widget to place the background image
        # self.canvas = tk.Canvas(self, width=600, height=600)
        # self.canvas.pack(fill="both", expand=True)
        # self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, text="ImageImageImageImageImage", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=8, pady=10, padx=10)
        tk.Label(self, text="Register", font=("Helvetica", 16)).grid(row=0, column=9, columnspan=4, pady=10)

        tk.Label(self, text="Username:").grid(row=1, column=9, sticky="e")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=10, pady=5)

        tk.Label(self, text="Password:").grid(row=2, column=9, sticky="e")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=10, pady=5)

        login_button = tk.Button(self, text="Login", command=self.join_now)
        login_button.grid(row=3, column=9, columnspan=2, pady=10)

    def join_now(self):
        self.callback.type = 'register'
        self.callback.data = {'username': self.username_entry.get(), 'password': self.password_entry.get()}
        self.callback.function()
