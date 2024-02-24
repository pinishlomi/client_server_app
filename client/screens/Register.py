import pathlib, os
import tkinter as tk
from client_server_app.client.screens import Callback
from PIL import Image, ImageTk


class Register(tk.Frame):
    def __init__(self, callback: Callback):
        super().__init__()
        self.callback = callback
        self.password_entry = None
        self.username_entry = None
        self.canvas = None
        self.background_photo = None
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

        # Load your image
        # Get the absolute path of the image file relative to the project's root folder
        project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        image_path = f'{project_dir}/assets/images/sign_up.png'
        original_image = Image.open(image_path)
        # Resize the image to fit 2/3 of the width
        image_width = int(self.winfo_screenwidth() * 2 / 3)
        image_height = int(original_image.size[1] * image_width / original_image.size[0])
        resized_image = original_image.resize((image_width, image_height))
        # Convert image to Tkinter format
        self.background_photo = ImageTk.PhotoImage(resized_image)
        tk.Label(self, image=self.background_photo).grid(row=0, column=0, columnspan=8, rowspan=10, pady=10, padx=10)
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
