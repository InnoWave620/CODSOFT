import random  # Import the random module for generating random characters
import string  # Import the string module for accessing string constants
import tkinter as tk  # Import the tkinter module for creating GUI applications
from tkinter import messagebox  # Import the messagebox module for displaying message dialogs

# Function to generate a random password of specified length
def generate_password(length):
    # Define the characters to be used for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))
    return password  # Return the generated password

# Function to generate a password based on user input and display it in the GUI
def generate_password_gui():
    length = length_entry.get()  # Get the password length entered by the user
    try:
        length = int(length)  # Convert the length to an integer
        if length <= 0:  # Check if the length is not positive
            messagebox.showwarning("Warning", "Please enter a positive integer.")
            return  # Exit the function if the length is not valid
        password = generate_password(length)  # Generate a password of the specified length
        result_label.config(text=f"Generated Password: {password}")  # Display the generated password
    except ValueError:
        # If the entered value is not a valid integer, show a warning message
        messagebox.showwarning("Warning", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")  # Set the title of the window

# Label prompting the user to enter the password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=5)  # Add padding and display the label in the window

# Entry field for the user to input the password length
length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)  # Add padding and display the entry field in the window

# Button to trigger the generation of the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=5)  # Add padding and display the button in the window

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=5)  # Add padding and display the label in the window

# Start the Tkinter event loop
root.mainloop()
