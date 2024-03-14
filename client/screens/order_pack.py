import tkinter as tk
from tkinter import ttk
from customtkinter import CustomStyle
from tkinter import messagebox


def create_start_date(root):
    start_frame = tk.Frame(root, bg="beige")
    start_frame.pack(fill="x", padx=20, pady=(10, 5))

    start_label = tk.Label(start_frame, text="Start Date:", bg="beige", font=("Arial", 16))
    start_label.pack(side="left", padx=(0, 10))

    start_entry = ttk.Entry(start_frame, style="Custom.TEntry", font=("Arial", 16))
    start_entry.pack(side="left")


def create_end_date(root):
    end_frame = tk.Frame(root, bg="beige")
    end_frame.pack(fill="x", padx=20, pady=5)

    end_label = tk.Label(end_frame, text="End Date:", bg="beige", font=("Arial", 16))
    end_label.pack(side="left", padx=(0, 10))

    end_entry = ttk.Entry(end_frame, style="Custom.TEntry", font=("Arial", 16))
    end_entry.pack(side="left")


def create_number_of_adults(root):
    adults_frame = tk.Frame(root, bg="beige")
    adults_frame.pack(fill="x", padx=20, pady=5)

    adults_label = tk.Label(adults_frame, text="Number of Adults:", bg="beige", font=("Arial", 16))
    adults_label.pack(side="left", padx=(0, 10))

    adults_combobox = ttk.Combobox(adults_frame, values=list(range(1, 11)), state="readonly", font=("Arial", 16))
    adults_combobox.current(0)  # Default value
    adults_combobox.pack(side="left")


def create_number_of_kids(root):
    kids_frame = tk.Frame(root, bg="beige")
    kids_frame.pack(fill="x", padx=20, pady=5)

    kids_label = tk.Label(kids_frame, text="Number of Kids:", bg="beige", font=("Arial", 16))
    kids_label.pack(side="left", padx=(0, 10))

    kids_combobox = ttk.Combobox(kids_frame, values=list(range(1, 11)), state="readonly", font=("Arial", 16))
    kids_combobox.current(0)  # Default value
    kids_combobox.pack(side="left")


def create_number_of_rooms(root):
    rooms_frame = tk.Frame(root, bg="beige")
    rooms_frame.pack(fill="x", padx=20, pady=5)

    rooms_label = tk.Label(rooms_frame, text="Number of Rooms:", bg="beige", font=("Arial", 16))
    rooms_label.pack(side="left", padx=(0, 10))

    rooms_combobox = ttk.Combobox(rooms_frame, values=list(range(1, 6)), state="readonly", font=("Arial", 16))
    rooms_combobox.current(0)  # Default value
    rooms_combobox.pack(side="left")


def create_meals(root):
    meals_frame = tk.Frame(root, bg="beige")
    meals_frame.pack(fill="x", padx=20, pady=5)

    meals_label = tk.Label(meals_frame, text="Meals:", bg="beige", font=("Arial", 16))
    meals_label.pack(side="left", padx=(0, 10))

    # Create Checkbuttons for each meal option
    meals = ["Breakfast", "Lunch", "Dinner"]
    for meal in meals:
        meal_var = tk.BooleanVar()
        meal_checkbox = tk.Checkbutton(meals_frame, text=meal, variable=meal_var, onvalue=True, offvalue=False,
                                       bg="beige", font=("Arial", 16))
        meal_checkbox.pack(side="left", padx=(0, 10))


def create_view(root):
    view_frame = tk.Frame(root, bg="beige")
    view_frame.pack(fill="x", padx=20, pady=5)

    view_label = tk.Label(view_frame, text="View:", bg="beige", font=("Arial", 16))
    view_label.pack(side="left", padx=(0, 10))

    # Create Radiobuttons for the view options
    view_options = ["Pool", "Sea", "No View"]
    view_var = tk.StringVar(value="No View")  # Default value
    for option in view_options:
        view_radiobutton = tk.Radiobutton(view_frame, text=option, variable=view_var, value=option, bg="beige",
                                          font=("Arial", 16))
        view_radiobutton.pack(side="left", padx=(0, 10))


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Reservation Details")

    # Set the size of the window
    window_width = 1000
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")

    # Set the background color
    root.configure(bg="beige")

    # CustomStyle object to customize the appearance
    style = CustomStyle()
    style.set_theme("light")  # Set theme to light

    # Customize the Entry widget appearance
    style.configure(
        "Custom.TEntry",
        padding=10,
        foreground="black",
        background="white",
        border_color="black",
        border_width=2,
        focus_color="blue",
        focus_thickness=2,
        font=("Arial", 16)
    )

    # Create a frame to contain the title
    title_frame = tk.Frame(root, bg="beige")
    title_frame.pack(fill="x", pady=20)

    # Create a label for the title
    title_label = tk.Label(title_frame, text="Reservation Details", bg="beige", font=("Arial", 20))
    title_label.pack()

    # Create start date field
    create_start_date(root)

    # Create end date field
    create_end_date(root)

    # Create number of adults field
    create_number_of_adults(root)

    # Create number of kids field
    create_number_of_kids(root)

    # Create number of rooms field
    create_number_of_rooms(root)

    # Create meals field
    create_meals(root)

    # Create view field
    create_view(root)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
