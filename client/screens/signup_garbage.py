import tkinter as tk
from tkinter import font
from tkinter import messagebox

# Function to be executed when the "Continue" button is pressed
def continue_button_clicked():
    # Get the entered email and password
    entered_email = email_entry.get()
    entered_password = password_entry.get()

    # Check if the email ends with "@gmail.com"
    if not entered_email.endswith("@gmail.com"):
        messagebox.showwarning("Invalid Email", "Please enter a valid Gmail email address.")
    # Check if the password is less than 6 characters
    elif len(entered_password) < 6:
        messagebox.showwarning("Invalid Password", "Password should be at least 6 characters long.")
    else:
        messagebox.showinfo("Success", "Email and password are valid! You can continue.")

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("1000x700")

# Set the background color to beige
root.configure(bg='beige')

# Set the title font
title_font = font.Font(family="Abril Fatface", size=22)

# Create and place the title label using grid
title_label = tk.Label(root, text="Sign Up", font=title_font, bg='beige')
title_label.grid(row=0, column=0, padx=750, pady=200)  # Adjust padx and pady for positioning

# Create and place the email label and entry using grid
email_label = tk.Label(root, text="Email:", bg='beige')
email_label.grid(row=1, column=0, pady=(10, 0))  # Adjust pady for vertical positioning

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=0, pady=(0, 10), padx=750)  # Adjust pady for vertical positioning and padx for horizontal positioning

# Create and place the password label and entry using grid
password_label = tk.Label(root, text="Password:", bg='beige')
password_label.grid(row=3, column=0, pady=(10, 0))  # Adjust pady for vertical positioning

password_entry = tk.Entry(root, show="*")  # The 'show' parameter hides the password characters
password_entry.grid(row=4, column=0, pady=(0, 10), padx=750)  # Adjust pady for vertical positioning and padx for horizontal positioning

# Create and place the "Continue" button using grid
continue_button = tk.Button(root, text="Continue", command=continue_button_clicked)
continue_button.grid(row=5, column=0, pady=(10, 0), padx=750)  # Adjust pady for vertical positioning and padx for horizontal positioning

# Run the Tkinter event loop
root.mainloop()