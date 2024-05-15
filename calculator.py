import tkinter as tk  # Import the tkinter module for creating GUI applications

# Function to handle button clicks
def on_click(event):
    text = event.widget.cget("text")  # Get the text of the clicked button
    if text == "=":  # If the clicked button is "=", evaluate the expression
        try:
            result = eval(entry.get())  # Evaluate the expression in the entry field
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, str(result))  # Insert the result into the entry field
        except Exception as e:
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, "invalid equation!")  # Display "invalid equation!" if evaluation fails
            
    elif text == "C":  # If the clicked button is "C", clear the entry field
        entry.delete(0, tk.END)  # Clear the entry field
    else:  # For other buttons, insert their text into the entry field
        entry.insert(tk.END, text)  # Insert the text of the clicked button into the entry field

# Create the main window
root = tk.Tk()
root.title("Calculator")  # Set the title of the window
root.configure(background='orange')  # Set the background color of the window

# Entry field for displaying and inputting expressions
entry = tk.Entry(root, font=("Sans", 16))
entry.grid(row=0, column=0, columnspan=4, sticky="ew")  # Position the entry field in the window

# Define the buttons for the calculator
buttons = [
    "7", "8", "9", "/",  # Row 1
    "4", "5", "6", "*",  # Row 2
    "1", "2", "3", "-",  # Row 3
    "C", "0", "=", "+"   # Row 4
]

# Create and position the buttons in the window
for i in range(4):
    for j in range(4):
        button = tk.Button(root, text=buttons[i*4 + j], font=("Arial", 16), width=5, height=2)
        button.grid(row=i+1, column=j, sticky="nsew")  # Position the button in the window
        button.bind("<Button-1>", on_click)  # Bind the button click event to the on_click function

# Start the Tkinter event loop
root.mainloop()




