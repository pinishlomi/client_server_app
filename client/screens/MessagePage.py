import tkinter as tk
from client_server_app.client.screens import Callback


class MessagePage(tk.Frame):
    def __init__(self, callback: Callback):
        super().__init__()
        self.send_button = None
        self.message_entry = None
        self.input_frame = None
        self.messages = None
        self.scrollbar = None
        self.message_frame = None
        self.canvas = None
        self.callback = callback
        self.show()

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, text="Message Page", font=("Helvetica", 26)).grid(row=0, column=0, columnspan=10, pady=10)

        # send_message_button = tk.Button(self, text="Send Message", command=self.send_message)
        # send_message_button.grid(row=3, column=0, columnspan=2, pady=10)
        # Create a canvas to contain the chat messages
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Add a frame inside the canvas to hold the messages
        self.message_frame = tk.Frame(self.canvas)

        # Attach the canvas to a scrollbar
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Make the message frame a window in the canvas
        self.canvas.create_window((0, 0), window=self.message_frame, anchor=tk.NW)

        # Example: Adding some sample messages
        self.messages = []
        # Create a frame to hold the message input field and send button
        self.input_frame = tk.Frame(self)
        self.input_frame.grid(row=1, column=0, sticky="ew")

        # Input field for typing messages
        self.message_entry = tk.Entry(self.input_frame)
        self.message_entry.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=10)

        # Button to send messages
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=0, column=1, padx=(5, 10), pady=10)

        # Configure resizing behavior
        self.grid_rowconfigure(0, weight=1)
        self.input_frame.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Bind the canvas to the event of resizing
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def send_message(self):
        message = self.message_entry.get().strip()
        if message:
            self.add_message("You", message)
            self.message_entry.delete(0, tk.END)  # Clear the input field after sending

            self.callback.type = 'message'
            self.callback.data = message
            self.callback.function()

    def add_message(self, sender, message):
        """Add a message to the message frame."""
        sender_label = tk.Label(self.message_frame, text=sender + ":", font=("Arial", 12, "bold"))
        sender_label.grid(sticky="w", padx=(10, 0), pady=(5, 0))

        message_label = tk.Label(self.message_frame, text=message, wraplength=400, justify="left")
        message_label.grid(sticky="w", padx=(5, 10), pady=(5, 0))

        # Update the scroll region after adding the message
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Scroll to the bottom
        self.canvas.yview_moveto(1.0)

    def on_canvas_configure(self, event):
        """Update the scroll region when the size of the canvas changes."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
