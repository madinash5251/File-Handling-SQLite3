# Importing necessary modules
import tkinter as tk  # Importing the Tkinter module for GUI
import app.functions as functions  # Importing custom functions from the app module

# Main function to run the To-Do List application
def main():
    # Creating the main window for the To-Do List application
    root = tk.Tk()
    root.title("To-Do List")  # Setting the default title of the application window
    root.geometry("600x600")  # Setting the default size of the application window

    # Asking the user to input their name using a pop-up dialog box
    user_name = prompt_user_for_name(root)

    # Adjusting the title of the application window based on user input
    if user_name:
        root.title(f"{user_name}'s To-Do List")  # Setting the window title with user's name
    else:
        root.title("To-Do List")  # Keeping the default title if no user name provided

    # Setting up the graphical user interface (GUI) for the To-Do List application
    functions.setup_gui(root)  # Calling the function to set up the GUI components

    # Running the main event loop to display the GUI and handle user interactions
    root.mainloop()


# Function to prompt the user to input their name
def prompt_user_for_name(root):
    # Using the Tkinter simpledialog to create a pop-up for user input
    user_name = tk.simpledialog.askstring("Welcome!", "Please enter your name:")
    return user_name  # Returning the user-provided name or None if canceled


# Checking if the script is being run directly
if __name__ == "__main__":
    main()  # Calling the main function to start the To-Do List application
