import pathlib
import tkinter as tk
from client_server_app.client.screens import Callback
from PIL import Image, ImageTk
import customtkinter as ctk


class Register():
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.root = root
        self.callback = callback
        self.password_entry = None
        self.username_entry = None
        self.canvas = None
        self.background_photo = None
        self.show()

    def show(self):
        self.root.configure(bg='beige')
        print(f'register : {self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        # Load your image
        # Get the absolute path of the image file relative to the project's root folder
        project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        image_path = f'{project_dir}/assets/images/sign_up.png'
        original_image = Image.open(image_path)
        # Resize the image to fit 2/3 of the width
        image_width = int(self.root.winfo_screenwidth() * 2 / 3)
        image_height = int(original_image.size[1] * image_width / original_image.size[0])
        resized_image = original_image.resize((image_width, self.root.winfo_screenheight()))
        # resized_image = original_image.resize((image_width, self.winfo_screenheight()))
        # Convert image to Tkinter format
        self.background_photo = ImageTk.PhotoImage(resized_image)
        image_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        image_frame.pack(fill='both', side=tk.LEFT)
        # image_frame.configure(bg=)
        image = tk.Label(image_frame, image=self.background_photo, background='beige')
        image.pack(side=tk.LEFT)

        register_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        register_frame.pack(pady=40, padx=40, fill='both', expand=True, side=tk.LEFT)
        title_font = ('Abril Fatface', 28)
        filed_font = ('Abril Fatface', 20)

        space = ctk.CTkLabel(master=register_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=10)

        label = ctk.CTkLabel(master=register_frame, font=title_font, text='Sign up', padx=10, pady=5)
        label.pack(pady=12, padx=10)

        username_lbl = ctk.CTkLabel(master=register_frame,font=filed_font, text='Username:')
        username_lbl.pack(anchor=tk.W, padx=10)
        self.username_entry = ctk.CTkEntry(master=register_frame,font=filed_font)
        self.username_entry.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=register_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        password_lbl = ctk.CTkLabel(master=register_frame,font=filed_font, text='Password:')
        password_lbl.pack(anchor=tk.W, padx=10)
        self.password_entry = ctk.CTkEntry(master=register_frame,font=filed_font, show="*")
        self.password_entry.pack(anchor=tk.W, padx=10)

        sign_on_btn_frame = ctk.CTkFrame(master=register_frame, fg_color='beige')
        sign_on_btn_frame.pack(pady=60, padx=40, fill='both', expand=True)
        sign_on_btn = ctk.CTkButton(master=sign_on_btn_frame, font=title_font, text='Sign Up',
                               fg_color='#e9e9e9', text_color='black', command=self.join_now)
        sign_on_btn.pack(pady=40, padx=10)

    def join_now(self):
        self.callback.type = 'register'
        self.callback.data = {'username': self.username_entry.get(), 'password': self.password_entry.get()}
        self.callback.function()
