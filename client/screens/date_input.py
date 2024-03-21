import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def show_selected_date():
    selected_date = cal.get_date()
    print(f"Selected date: {selected_date}")

root = tk.Tk()
root.title("Date Picker Example")

# Create a DateEntry widget
cal = DateEntry(root, date_pattern="yyyy-mm-dd")
cal.pack(padx=10, pady=10)

# Button to retrieve the selected date
ttk.Button(root, text="Get Date", command=show_selected_date).pack(padx=10, pady=10)

root.mainloop()
