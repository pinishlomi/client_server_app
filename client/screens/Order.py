import pathlib
import tkinter as tk
from datetime import timedelta
from tkinter import ttk
import tkinter.messagebox as tkmb
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date
from utils.Callback import Callback


class Order(tk.Frame):


    """
    Entry claim: gets root, callback: Callback
    Exit claim: The operation activates the inheriting class (tk.frame),
    receives the callback resets variables to none and calls the show function
    """
    def __init__(self, root, callback: Callback):
        super().__init__()
        self.root = root
        self.callback = callback
        self.selected_start_date = None
        self.selected_end_date = None
        self.start_date_entry = None
        self.end_date_entry = None
        self.num_adults_var = None
        self.num_kids_var = None
        self.num_rooms_var = None
        self.checkboxes_meal = {}
        self.canvas = None
        self.background_photo = None
        self.show()

    """
    Entry claim: None
    Exit claim: sets and shows the screen
    """
    def show(self):
        self.root.configure(bg='beige')

        # Load your image
        project_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        image_path = f'{project_dir}/assets/images/sign_up.png'
        original_image = Image.open(image_path)
        image_width = int(self.root.winfo_screenwidth())
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
        self.selected_start_date = self.start_date_entry.get_date()
        self.start_date_entry.pack(anchor=tk.W, padx=10)
        self.start_date_entry.bind("<<DateEntrySelected>>", self.on_start_date)

        space = ctk.CTkLabel(master=left_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_adults_lbl = ctk.CTkLabel(master=left_frame, font=filed_font, text='Number Of Adults:', text_color='black')
        num_adults_lbl.pack(anchor=tk.W, padx=10)
        self.num_adults_var = tk.StringVar()
        num_children_options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        num_adults_combo = ttk.Combobox(left_frame, values=num_children_options, width=5,
                                        textvariable=self.num_adults_var)
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
        self.selected_end_date = self.end_date_entry.get_date()
        self.end_date_entry.bind("<<DateEntrySelected>>", self.on_end_date)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_kids_lbl = ctk.CTkLabel(master=right_frame, font=filed_font, text='Number Of Kids:', text_color='black')
        num_kids_lbl.pack(anchor=tk.W, padx=10)
        self.num_kids_var = tk.StringVar()
        num_kids_combo = ttk.Combobox(right_frame, values=num_children_options, width=5, textvariable=self.num_kids_var)
        num_kids_combo.current(0)
        num_kids_combo.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        num_rooms_lbl = ctk.CTkLabel(master=right_frame, font=filed_font, text='Number Of Rooms:', text_color='black')
        num_rooms_lbl.pack(anchor=tk.W, padx=10)
        self.num_rooms_var = tk.StringVar()
        num_rooms_options = ['1', '2', '3', '4', '5']
        num_rooms_combo = ttk.Combobox(right_frame, values=num_rooms_options, width=5, textvariable=self.num_rooms_var)
        num_rooms_combo.current(0)
        num_rooms_combo.pack(anchor=tk.W, padx=10)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        space = ctk.CTkLabel(master=right_frame, font=filed_font, text='', text_color='black')
        space.pack(anchor=tk.W, pady=5)

        order_btn = ctk.CTkButton(master=main_frame, font=title_font, text='Submit Reservation',
                                  fg_color='#e9e9e9', text_color='black', command=self.order)
        order_btn.pack(pady=0, padx=10)

    """
    Entry claim: get event from the user
    Exit claim: check if the start dates are invalid.
    show a messagebox if the dates are invalid.
    """
    def on_start_date(self, event):
        current_selected_date = self.start_date_entry.get_date()
        selected_end_date = self.end_date_entry.get_date()
        if current_selected_date < date.today():
            self.start_date_entry.set_date(self.selected_start_date)
            tkmb.showerror(title="Invalid Date",
                           message="Start date should be after or equals to current day")
        elif current_selected_date > selected_end_date:
            self.start_date_entry.set_date(self.selected_start_date)
            tkmb.showerror(title="Invalid Date",
                           message="Start date should be before or equals to end date,\n Please correct to valid date")
        else:
            self.selected_start_date = current_selected_date

    """
    Entry claim: get event from the user
    Exit claim: check if the end dates are invalid.
    show a messagebox if the dates are invalid.
    """
    def on_end_date(self, event):
        current_selected_date = self.end_date_entry.get_date()
        if current_selected_date < date.today():
            self.end_date_entry.set_date(self.selected_end_date)
            tkmb.showerror(title="Invalid Date",
                           message="Start date should be after or equals to current day")
        elif current_selected_date < self.selected_start_date:
            self.end_date_entry.set_date(self.selected_end_date)
            tkmb.showerror(title="Invalid Date",
                           message="End date should be after or equals to start date,\n Please correct to valid date")
        else:
            self.selected_end_date = current_selected_date

    """
    Entry claim: None
    Exit claim: Updates the callback with the appropriate type and data for the user order
    with the data that the user putted and calls the callback function.
    """
    def order(self):
        # Collect selected meals
        selected_meals = []
        for checkbox, var in self.checkboxes_meal.items():
            if var.get():
                selected_meals.append(checkbox)

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
