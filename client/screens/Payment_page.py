import tkinter as tk


def submit_payment():
    # Placeholder function for submitting payment
    print("Payment submitted")


def create_payment_page():
    # Create Tkinter window
    window = tk.Tk()
    window.title("Checkout")  # Set window title to "Checkout"

    # Set window size and position
    window.geometry("1000x700")  # Updated size to 1000x700
    window.configure(bg="beige")  # Set background color to beige

    # Add widgets or components to the window
    title_label = tk.Label(window, text="Welcome to the Payment Page!", font=("Helvetica", 20), bg="beige")
    title_label.pack(pady=20)

    # Entry field for ID
    id_label = tk.Label(window, text="ID:", bg="beige", font=("Helvetica", 14))
    id_label.pack(pady=(0, 10))
    id_entry = tk.Entry(window, width=30, font=("Helvetica", 14))
    id_entry.pack(pady=(0, 10))

    # Entry field for card number
    card_label = tk.Label(window, text="Card Number:", bg="beige", font=("Helvetica", 14))
    card_label.pack(pady=(0, 10))
    card_entry = tk.Entry(window, width=30, font=("Helvetica", 14))
    card_entry.pack(pady=(0, 10))

    # Entry field for card expiration date
    expiry_label = tk.Label(window, text="Expiry Date (MM/YY):", bg="beige", font=("Helvetica", 14))
    expiry_label.pack(pady=(0, 10))
    expiry_entry = tk.Entry(window, width=10, font=("Helvetica", 14))
    expiry_entry.pack(pady=(0, 10))

    # Entry field for CVC
    cvc_label = tk.Label(window, text="CVC:", bg="beige", font=("Helvetica", 14))
    cvc_label.pack(pady=(0, 10))
    cvc_entry = tk.Entry(window, width=5, font=("Helvetica", 14))
    cvc_entry.pack(pady=(0, 10))

    # Label for displaying price
    price_label = tk.Label(window, text="Price: $50.00", font=("Helvetica", 14), bg="beige")
    price_label.pack(pady=(20, 0))

    # Submit button
    submit_button = tk.Button(window, text="Submit Payment", command=submit_payment, font=("Helvetica", 16))
    submit_button.pack(pady=20)

    # Run the Tkinter event loop
    window.mainloop()


# Create the payment page
create_payment_page()
