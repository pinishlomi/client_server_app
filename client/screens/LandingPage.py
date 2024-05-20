import pathlib
from PIL import Image, ImageTk
import tkinter as tk
import customtkinter as ctk
from client_server_app.client import Callback


"""
Entry claim: 
Exit claim: 
"""
class LandingPage(tk.Frame):


    """
    Entry claim: gets root, callback
    Exit claim: The operation activates the inheriting class (tk.frame), receives the callback and the root,
    initializes that the screen size cannot be changed and calls the show function
    """
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.callback = callback
        self.root = root
        root.resizable(False, False)
        self.show()

    """
    Entry claim: None
    Exit claim: Shows the screen
    """
    def show(self):
        self.root.configure(bg='beige')

        tk.Label(self, text="Landing Page", font=("Helvetica", 26)).grid(row=0, column=0, columnspan=10, pady=10)
        if self.callback.data and self.callback.data.get('user_authenticate', False):
            pass
            # show somthing else
        else:
            # Load your image
            # Get the absolute path of the image file relative to the project's root folder
            project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
            image_path = f'{project_dir}/assets/images/landing_background.jpeg'
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

            landing_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
            landing_frame.pack(pady=40, padx=40, fill='both', expand=True, side=tk.LEFT)
            title_font = ('Abril Fatface', 28)
            filed_font = ('Abril Fatface', 20)

            space = ctk.CTkLabel(master=landing_frame, font=filed_font, text='')
            space.pack(anchor=tk.W, pady=10)

            label = ctk.CTkLabel(master=landing_frame, font=title_font, text='Welcome to Wolf Hotel!', text_color='black',  padx=10, pady=5)
            label.pack(pady=12, padx=10)

            sign_on_btn = ctk.CTkButton(master=landing_frame, font=title_font, text='Sign in',
                                   fg_color='#e9e9e9', text_color='black', command=self.sign_in)
            sign_on_btn.pack(pady=40, padx=10)
            sign_on_btn = ctk.CTkButton(master=landing_frame, font=title_font, text='Register',
                                   fg_color='#e9e9e9', text_color='black', command=self.join_now)
            sign_on_btn.pack(pady=40, padx=10)

    """
    Entry claim: None
    Exit claim: Updates the callback with the appropriate data and calls it
    """
    def sign_in(self):
        self.callback.type = 'sign_in'
        self.callback.data = 'Sign in clicked'
        self.callback.function()

    """
    Entry claim: None
    Exit claim: Updates the callback with the appropriate data and calls it
    """
    def join_now(self):
        self.callback.type = 'sign_up'
        self.callback.data = 'register clicked'
        self.callback.function()
