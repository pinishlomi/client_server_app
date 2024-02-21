import tkinter as tk
from PIL import ImageTk, Image

def resize_image(image, width, height):
    return image.resize((width, height))

root = tk.Tk()
root.title("Tkinter Image Demo")

def register():
    # Function to handle registration process
    print("Registration Process")


# Load your image
original_image = Image.open("background_image.jpg")
# Resize the image to fit 2/3 of the width
root.geometry('1536x900')
print(root.winfo_screenwidth())
print(root.winfo_screenwidth())
image_width = int(root.winfo_screenwidth() * 2 / 3)
image_height = int(original_image.size[1] * image_width / original_image.size[0])
resized_image = resize_image(original_image, image_width, image_height)
# Convert image to Tkinter format
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(root, image=tk_image)
image_label.grid(row=0, column=0, columnspan=2)

# Add registration widgets
registration_frame = tk.Frame(root, padx=20, pady=10)
registration_frame.grid(row=0, column=2, sticky="nsew")

tk.Label(registration_frame, text="Username:").grid(row=0, column=0, sticky="e")
tk.Entry(registration_frame).grid(row=0, column=1)

tk.Label(registration_frame, text="Password:").grid(row=1, column=0, sticky="e")
tk.Entry(registration_frame, show="*").grid(row=1, column=1)

tk.Label(registration_frame, text="Email:").grid(row=2, column=0, sticky="e")
tk.Entry(registration_frame).grid(row=2, column=1)

register_button = tk.Button(registration_frame, text="Register", command=register)
register_button.grid(row=3, columnspan=2)

root.mainloop()
