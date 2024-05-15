import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()  # Get the task from the entry field
    if task:  # Check if the task is not empty
        listbox.insert(tk.END, task)  # Insert the task into the listbox at the end
        task_entry.delete(0, tk.END)  # Clear the entry field after adding the task
    else:
        # If the task is empty, show a warning message
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task from the list
def delete_task():
    try:
        index = listbox.curselection()[0]  # Get the index of the selected task
        listbox.delete(index)  # Delete the task from the listbox
    except IndexError:
        # If no task is selected, show a warning message
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to update a task in the list
# Function to update a task in the list
def update_task():
    try:
        index = listbox.curselection()[0]  # Get the index of the selected task
        task = task_entry.get()  # Get the new task from the entry field
        if task:  # Check if the new task is not empty
            listbox.delete(index)  # Delete the old task from the listbox
            listbox.insert(index, task)  # Insert the new task at the same index
            task_entry.delete(0, tk.END)  # Clear the entry field after updating
        else:
            # If the new task is empty, show a warning message
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        # If no task is selected, show a warning message
        messagebox.showwarning("Warning", "Please select a task to update.")


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry field to input tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Button to add a task
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Button to delete a task
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Button to update a task
update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

