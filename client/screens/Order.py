import pathlib
import tkinter as tk
from datetime import datetime, date, timedelta
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from client_server_app.client.screens import Callback
from PIL import Image, ImageTk
import customtkinter as ctk
def on_start_date(event):
    print(f"Selected date: ")

class Order(tk.Frame):
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.root = root
        self.callback = callback
        self.start_date_entry = None
        self.end_date_entry = None
        self.num_adults_entry = None
        self.num_adults_var = None
        self.num_kids = None
        self.num_rooms = None
        self.view = None
        self.selected_meals = None
        self.canvas = None
        self.background_photo = None
        self.show()

    def show(self):
        self.root.configure(bg='beige')
        print(f'Login : {self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')
        # Load your image
        # Get the absolute path of the image file relative to the project's root folder
        project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        image_path = f'{project_dir}/assets/images/sign_up.png'
        original_image = Image.open(image_path)
        # Resize the image to fit 2/3 of the width
        image_width = int(self.root.winfo_screenwidth())
        image_height = int(original_image.size[1] * image_width / original_image.size[0])
        resized_image = original_image.resize((image_width, int(self.root.winfo_screenheight() * 1 / 4)))
        # resized_image = original_image.resize((image_width, self.winfo_screenheight()))
        # Convert image to Tkinter format
        self.background_photo = ImageTk.PhotoImage(resized_image)
        image_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        image_frame.pack(fill='both', side=tk.TOP)
        # image_frame.configure(bg=)
        image = tk.Label(image_frame, image=self.background_photo, background='beige')
        image.pack(side=tk.LEFT)

        main_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        main_frame.pack(padx=40, fill='both', expand=True, side=tk.LEFT)
        title_font = ('Abril Fatface', 28)
        filed_font = ('Abril Fatface', 20)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=10)

        label = ctk.CTkLabel(master=main_frame, font=title_font, text='Reservation Details', padx=10, pady=5)
        label.pack(padx=10)

        start_date_lbl = ctk.CTkLabel(master=main_frame, font=filed_font, text='Start Date:')
        start_date_lbl.pack(anchor=tk.W, padx=10)
        self.start_date_entry = DateEntry(main_frame, date_pattern="dd-mm-yyyy")
        self.start_date_entry.pack(anchor=tk.W, padx=10)
        self.start_date_entry.bind("<<DateEntrySelected>>", self.on_start_date)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        end_date_lbl = ctk.CTkLabel(master=main_frame, font=filed_font, text='End Date:')
        end_date_lbl.pack(anchor=tk.W, padx=10)
        self.end_date_entry = DateEntry(main_frame, date_pattern="dd-mm-yyyy")
        self.end_date_entry.pack(anchor=tk.W, padx=10)
        self.end_date_entry.set_date(self.start_date_entry.get_date() + timedelta(days=7))
        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        num_adults_lbl = ctk.CTkLabel(master=main_frame, font=filed_font, text='Number Of Adults:')
        num_adults_lbl.pack(anchor=tk.W, padx=10)
        # self.num_adults_var.set('1')
        GENDER_OPTIONS = ['1', '2', '3', '4', '5', '6']
        num_adults_combo = ttk.Combobox(main_frame, values=GENDER_OPTIONS, width=5,
                                        textvariable=self.num_adults_var)
        num_adults_combo.current(0)
        num_adults_combo.pack(anchor=tk.W, padx=10)

        self.num_adults_entry = ctk.CTkEntry(master=main_frame, font=filed_font, show="*")
        self.num_adults_entry.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        num_kids_lbl = ctk.CTkLabel(master=main_frame, font=filed_font, text='Number Of Kids:')
        num_kids_lbl.pack(anchor=tk.W, padx=10)
        self.num_kids = ctk.CTkEntry(master=main_frame, font=filed_font, show="*")
        self.num_kids.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        num_rooms_lbl = ctk.CTkLabel(master=main_frame, font=filed_font, text='Number Of Rooms:')
        num_rooms_lbl.pack(anchor=tk.W, padx=10)
        self.num_rooms = ctk.CTkEntry(master=main_frame, font=filed_font, show="*")
        self.num_rooms.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='')
        space.pack(anchor=tk.W, pady=5)

        order_btn = ctk.CTkButton(master=main_frame, font=title_font, text='Submit Reservation',
                                    fg_color='#e9e9e9', text_color='black', command=self.order)
        order_btn.pack(pady=0, padx=10)

    def on_start_date(self, event):
        selected_date = self.start_date_entry.get_date()
        selected_end_date = self.end_date_entry.get_date()
        print(f"Selected date: {selected_date}, {selected_end_date}{type(selected_date)}")
        if selected_date > selected_end_date:
            print("error")
            self.end_date_entry.set_date(selected_date)
        else:
            print("ok")

    def order(self):
        pass
        # TODO validate data
        # TODO create new data object
        data = {
            'start_date': self.start_date_entry.get_date(),

        }
        # self.callback.type = 'order'
        # self.callback.data = {'order': data}
        # self.callback.function()


def main():
    root = tk.Tk()
    root.title("Reservation Details")
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    Order(root, None)
    root.mainloop()


if __name__ == '__main__':
    main()
