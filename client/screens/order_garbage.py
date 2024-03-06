import tkinter as tk
from tkinter import ttk


def process_reservation_details():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    num_adults = adults_entry.get()
    num_kids = kids_entry.get()
    num_rooms = rooms_entry.get()
    view = view_var.get()
    selected_meals = [meal_var.get() for meal_var in meal_vars]

    print("Start Date:", start_date)
    print("End Date:", end_date)
    print("Number of Adults:", num_adults)
    print("Number of Kids (up to 12 years old):", num_kids)
    print("Number of Rooms:", num_rooms)
    print("View:", view)
    print("Selected Meals:", selected_meals)


# Create the main window
root = tk.Tk()
root.title("Reservation Details")

# Set the window size
root.geometry("1000x700")

# Set the background color to beige
root.configure(bg='beige')

# Create and place widgets using the grid layout
tk.Label(root, text="Start Date:", bg='beige').grid(row=0, column=0, padx=10, pady=10)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="End Date:", bg='beige').grid(row=1, column=0, padx=10, pady=10)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Adults:", bg='beige').grid(row=2, column=0, padx=10, pady=10)
adults_entry = tk.Entry(root)
adults_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Kids (up to 12 years old):", bg='beige').grid(row=3, column=0, padx=10, pady=10)
kids_entry = tk.Entry(root)
kids_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Rooms:", bg='beige').grid(row=4, column=0, padx=10, pady=10)
rooms_entry = tk.Entry(root)
rooms_entry.grid(row=4, column=1, padx=10, pady=10)

# Checkbutton for selecting view
view_var = tk.StringVar()
tk.Label(root, text="Select View:", bg='beige').grid(row=5, column=0, padx=10, pady=10)
sea_checkbox = tk.Checkbutton(root, text="Sea", variable=view_var, onvalue="Sea", offvalue="")
sea_checkbox.grid(row=5, column=1, padx=10, pady=10)

pool_checkbox = tk.Checkbutton(root, text="Pool", variable=view_var, onvalue="Pool", offvalue="")
pool_checkbox.grid(row=5, column=2, padx=10, pady=10)

no_view_checkbox = tk.Checkbutton(root, text="No View", variable=view_var, onvalue="No View", offvalue="")
no_view_checkbox.grid(row=5, column=3, padx=10, pady=10)

# Checkbuttons for selecting meals
meal_vars = [tk.StringVar() for _ in range(3)]  # One for each meal
tk.Label(root, text="Select Meals:", bg='beige').grid(row=6, column=0, padx=10, pady=10)
breakfast_checkbox = tk.Checkbutton(root, text="Breakfast", variable=meal_vars[0], onvalue="Breakfast", offvalue="")
breakfast_checkbox.grid(row=6, column=1, padx=10, pady=10)

lunch_checkbox = tk.Checkbutton(root, text="Lunch", variable=meal_vars[1], onvalue="Lunch", offvalue="")
lunch_checkbox.grid(row=6, column=2, padx=10, pady=10)

dinner_checkbox = tk.Checkbutton(root, text="Dinner", variable=meal_vars[2], onvalue="Dinner", offvalue="")
dinner_checkbox.grid(row=6, column=3, padx=10, pady=10)

# Big Submit Button
submit_button = tk.Button(root, text="Submit Reservation", command=process_reservation_details, font=('Helvetica', 14),
                          bg='green', fg='white')
submit_button.grid(row=7, column=0, columnspan=4, pady=20)

# Bind the Return key to process_reservation_details function
root.bind('<Return>', lambda event=None: process_reservation_details())

# Start the Tkinter event loop
root.mainloop()
