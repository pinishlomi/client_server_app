import pathlib
import tkinter as tk
from datetime import timedelta
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from client_server_app.client.screens import Callback


def on_start_date(event):
    print(f"Selected date: ")


class Order(tk.Frame):
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.root = root
        self.callback = callback
        self.start_date_entry = None
        self.end_date_entry = None
        self.num_adults_var = None
        self.num_kids_var = None
        self.num_rooms_var = None
        self.checkboxes_meal = {}
        self.canvas = None
        self.background_photo = None
        self.show()

    def show(self):
        self.root.configure(bg='beige')
        print(f'Login : {self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}')

        # Load your image
        project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        image_path = f'{project_dir}/assets/images/sign_up.png'
        original_image = Image.open(image_path)
        image_width = int(self.root.winfo_screenwidth())
        image_height = int(original_image.size[1] * image_width / original_image.size[0])
        resized_image = original_image.resize((image_width, int(self.root.winfo_screenheight() * 1 / 4)))
        self.background_photo = ImageTk.PhotoImage(resized_image)

        image_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        image_frame.pack(fill='both', side=tk.TOP)
        image = tk.Label(image_frame, image=self.background_photo, background='beige')
        image.pack(side=tk.LEFT)

        main_frame = ctk.CTkFrame(master=self.root, fg_color='beige')
        main_frame.pack(padx=40, fill='both', expand=True, side=tk.LEFT)
        title_font = ('Abril Fatface', 28)
        filed_font = ('Abril Fatface', 20)

        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=10)

        label = ctk.CTkLabel(master=main_frame, font=title_font, text='Reservation Details', padx=10, pady=5,
                             text_color='black')
        label.pack(padx=10)
        space = ctk.CTkLabel(master=main_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        data_frame = ctk.CTkFrame(master=main_frame, fg_color='beige')
        data_frame.pack(padx=40, fill='both')

        left_frame = ctk.CTkFrame(master=data_frame, fg_color='beige')
        left_frame.pack(padx=80, expand=True, side=tk.LEFT)

        start_date_lbl = ctk.CTkLabel(master=left_frame, font=filed_font, text='Start Date:', text_color='black')
        start_date_lbl.pack(anchor=tk.W, padx=10)
        self.start_date_entry = DateEntry(left_frame, date_pattern="dd-mm-yyyy")
        self.start_date_entry.pack(anchor=tk.W, padx=10)
        self.start_date_entry.bind("<<DateEntrySelected>>", self.on_start_date)

        space = ctk.CTkLabel(master=left_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_adults_lbl = ctk.CTkLabel(master=left_frame, font=filed_font, text='Number Of Adults:', text_color='black')
        num_adults_lbl.pack(anchor=tk.W, padx=10)
        self.num_adults_var = tk.StringVar()
        GENDER_OPTIONS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        num_adults_combo = ttk.Combobox(left_frame, values=GENDER_OPTIONS, width=5, textvariable=self.num_adults_var)
        num_adults_combo.current(0)
        num_adults_combo.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=left_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)
        meals_lbl = ctk.CTkLabel(master=left_frame, font=filed_font, text='Select Meals:', text_color='black')
        meals_lbl.pack(anchor=tk.W, padx=10)

        # Create checkboxes using a loop
        meal_options = ['breakfast', 'lunch', 'dinner']
        for meal in meal_options:
            var = tk.IntVar()  # Create a variable to store checkbox state
            checkbox = ctk.CTkCheckBox(left_frame, text=meal, variable=var, hover_color='gray')
            checkbox.pack(anchor=tk.W, padx=10, pady=3)  # Add checkbox to the window
            self.checkboxes_meal[meal] = var  # Store checkbox and variable in dictionary

        right_frame = ctk.CTkFrame(master=data_frame, fg_color='beige')
        right_frame.pack(padx=40, expand=True, side=tk.LEFT)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)
        end_date_lbl = ctk.CTkLabel(master=right_frame, font=filed_font, text='End Date:', text_color='black')
        end_date_lbl.pack(anchor=tk.W, padx=10)
        self.end_date_entry = DateEntry(right_frame, date_pattern="dd-mm-yyyy")
        self.end_date_entry.pack(anchor=tk.W, padx=10)
        self.end_date_entry.set_date(self.start_date_entry.get_date() + timedelta(days=7))
        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_kids_lbl = ctk.CTkLabel(master=right_frame, font=filed_font, text='Number Of Kids:', text_color='black')
        num_kids_lbl.pack(anchor=tk.W, padx=10)
        self.num_kids_var = tk.StringVar()
        num_kids_combo = ttk.Combobox(right_frame, values=GENDER_OPTIONS, width=5, textvariable=self.num_kids_var)
        num_kids_combo.current(0)
        num_kids_combo.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_rooms_lbl = ctk.CTkLabel(master=right_frame, font=filed_font, text='Number Of Rooms:', text_color='black')
        num_rooms_lbl.pack(anchor=tk.W, padx=10)
        self.num_rooms_var = tk.StringVar()
        NUM_ROOMS_OPTIONS = ['1', '2', '3', '4', '5']
        num_rooms_combo = ttk.Combobox(right_frame, values=NUM_ROOMS_OPTIONS, width=5, textvariable=self.num_rooms_var)
        num_rooms_combo.current(0)
        num_rooms_combo.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
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
        # Collect selected meals
        selected_meals = []
        for checkbox, var in self.checkboxes_meal.items():
            if var.get():
                selected_meals.append(checkbox)

        # Print the selected meals for testing
        print(f'Selected meals: {selected_meals}')

        # Add code to handle the reservation with selected meals
        data = {
            'start_date': str(self.start_date_entry.get_date()),
            'end_date': str(self.end_date_entry.get_date()),
            'num_adults': self.num_adults_var.get(),
            'num_kids': self.num_kids_var.get(),
            'num_rooms': self.num_rooms_var.get(),
            'meals': selected_meals,
        }
        self.callback.type = 'order'
        self.callback.data = {'order': data}
        self.callback.function()


# def main():
#     root = tk.Tk()
#     root.title("Reservation Details")
#     root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
#     Order(root, None)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()
