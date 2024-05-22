import pathlib
import tkinter as tk
from utils.Callback import Callback
from PIL import Image, ImageTk
import customtkinter as ctk
import re
import tkinter.messagebox as tkmb



"""
Entry claim: 
Exit claim: handle with register screen data and shows it. 
"""
class Register():



    """
    Entry claim: gets root and callback
    Exit claim: The operation activates the inheriting class,
    receives the callback resets variables to none and calls the show function
    """
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.root = root
        self.callback = callback
        self.password_entry = None
        self.username_entry = None
        self.canvas = None
        self.background_photo = None
        self.show()

    """
    Entry claim: None
    Exit claim: sets and shows the screen
    """
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

        label = ctk.CTkLabel(master=register_frame, font=title_font, text='Register',text_color='black', padx=10, pady=5)
        label.pack(pady=12, padx=10)

        username_lbl = ctk.CTkLabel(master=register_frame, font=filed_font, text='Username:', text_color='black')
        username_lbl.pack(anchor=tk.W, padx=10)
        self.username_entry = ctk.CTkEntry(master=register_frame, font=filed_font, width=300)
        self.username_entry.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=register_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        password_lbl = ctk.CTkLabel(master=register_frame, font=filed_font, text='Password:', text_color='black')
        password_lbl.pack(anchor=tk.W, padx=10)
        self.password_entry = ctk.CTkEntry(master=register_frame, font=filed_font, show="*", width=300)
        self.password_entry.pack(anchor=tk.W, padx=10)

        sign_on_btn_frame = ctk.CTkFrame(master=register_frame, fg_color='beige')
        sign_on_btn_frame.pack(pady=60, padx=40, fill='both', expand=True)
        sign_on_btn = ctk.CTkButton(master=sign_on_btn_frame, font=title_font, text='Sign Up',
                                    fg_color='#e9e9e9', text_color='black', command=self.join_now)
        sign_on_btn.pack(pady=40, padx=10)


    """
    Entry claim: None
    Exit claim: Puts Username Eroor messagebox and Password Error messagebox
    if the username or the password doest meet the criteria. 
    if the password and the username meet the criteria, the def updates the callback with:
    the type, right data and calls it. 
    """
    def join_now(self):
        if not self.validate_username():
            tkmb.showerror(title="Username Error",
                           message="Username not match email format")
            return

        if not self.validate_password():
            tkmb.showerror(title="Password Error",
                           message="password not meets the following criteria:\n"
                                   "At least 8 characters long.\n"
                                   "Contains at least one uppercase letter, one lowercase letter, and one digit.")
            return

        username = self.username_entry.get()
        password = self.password_entry.get()
        self.callback.type = 'register'
        self.callback.data = {'username': username, 'password': password}
        self.callback.function()


    """
    Entry claim: None
    Exit claim: check if the username meets the username pattern (that I set) and return bool var.
    """
    def validate_username(self):
        # Validate email format using a regular expression
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, self.username_entry.get())

    """
    Entry claim: None
    Exit claim: check if the password meets the username pattern (that I set) and return bool var.
    """
    def validate_password(self):
        # Check password criteria
        password = self.password_entry.get()
        return (len(password) >= 8
                and any(c.isupper() for c in password)
                and any(c.islower() for c in password)
                and any(c.isdigit() for c in password))
