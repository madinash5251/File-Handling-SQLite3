# Importing necessary modules
import tkinter as tk  # Importing the Tkinter module for GUI
from tkinter import simpledialog  # Importing specific function for creating simple dialogs
import app.db as db  # Importing custom database functions from the app module

# Function to edit a task based on user input
def edit_task(event, listbox_tasks):
    selected_item = listbox_tasks.curselection()  # Getting the selected item from the listbox
    if selected_item:
        index = selected_item[0]
        task, time = listbox_tasks.get(index).split(" | ")  # Separating task and time from the selected item
        # Asking for user input to edit the task and time
        edited_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=task)
        edited_time = simpledialog.askstring("Edit Time", "Edit Time in Hours:", initialvalue=time.split()[0])
        # Verifying if edits are provided and then calling the database function to update the task
        if edited_task and edited_time:
            db.edit_task(task, time, edited_task, f"{edited_time} hours")  # Calling db function to edit the task
            load_tasks(listbox_tasks)  # Refreshing the tasks in the listbox

# Function to delete a task
def delete_item(listbox_tasks):
    selected_item = listbox_tasks.curselection()  # Getting the selected item from the listbox
    if selected_item:
        index = selected_item[0]
        full_item = listbox_tasks.get(index)
        task, time = full_item.split(" | ")  # Separating task and time from the selected item
        time = time.strip()  # Remove extra spaces from time

        db.delete_task(task, time)  # Calling db function to delete the task
        load_tasks(listbox_tasks)  # Refreshing the tasks in the listbox

# Function to add a new task
def add_task(entry_task, entry_time, listbox_tasks):
    task = entry_task.get()  # Getting the task from the Entry widget
    time = entry_time.get()  # Getting the time from the Entry widget
    if task and time:
        db.insert_task(task, f"{time} hours")  # Calling db function to insert a new task
        load_tasks(listbox_tasks)  # Refreshing the tasks in the listbox
        entry_task.delete(0, tk.END)  # Clearing the task Entry widget
        entry_time.delete(0, tk.END)  # Clearing the time Entry widget

# Function to load tasks into the listbox
def load_tasks(listbox_tasks):
    tasks = db.get_tasks()  # Getting tasks from the database
    listbox_tasks.delete(0, tk.END)  # Clearing the listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, f"{task[1]} | {task[2]}")  # Displaying Task and Time_in_Hours

# Function to set up the graphical user interface (GUI)
def setup_gui(root):
    # Creating labels, entry widgets, buttons, and listbox for the To-Do List application
    label_task = tk.Label(root, text="Enter Task:")  # Label for task
    label_task.pack()

    entry_task = tk.Entry(root, width=50)  # Entry widget for task
    entry_task.pack()

    label_time = tk.Label(root, text="Enter Time in Hours:")  # Label for time
    label_time.pack()

    entry_time = tk.Entry(root, width=50)  # Entry widget for time
    entry_time.pack()

    button_add = tk.Button(root, text="Add", command=lambda: add_task(entry_task, entry_time, listbox_tasks))
    button_add.pack()

    button_delete = tk.Button(root, text="Delete", command=lambda: delete_item(listbox_tasks))
    button_delete.pack()

    listbox_tasks = tk.Listbox(root, width=50)  # Listbox to display tasks
    listbox_tasks.pack()

    load_tasks(listbox_tasks)  # Loading tasks into the listbox

    listbox_tasks.bind('<Double-Button-1>', lambda event: edit_task(event, listbox_tasks))  # Binding double-click event
