# Importing SQLite3 module for database operations
import sqlite3

# Function to establish a connection to the database
def connect_db():
    return sqlite3.connect('todo.db')  # Connecting to the 'todo.db' SQLite database

# Function to create a 'todo' table if it doesn't exist in the database
def create_table():
    conn = connect_db()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries

    # SQL query to create a 'todo' table with ID, Task, and Time_in_Hours columns
    cursor.execute('''CREATE TABLE IF NOT EXISTS todo (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Task TEXT,
                    Time_in_Hours TEXT)''')
    conn.commit()  # Committing the changes to the database
    conn.close()  # Closing the connection to the database

# Function to insert a new task into the 'todo' table
def insert_task(task, time):
    conn = connect_db()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object

    # SQL query to insert a new task with its time into the 'todo' table
    cursor.execute("INSERT INTO todo (Task, Time_in_Hours) VALUES (?, ?)", (task, time))
    conn.commit()  # Committing the changes to the database
    conn.close()  # Closing the connection

# Function to delete a task from the 'todo' table based on task name and time
def delete_task(task, time):
    conn = connect_db()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object

    # SQL query to delete a task from the 'todo' table based on task name and time
    cursor.execute("DELETE FROM todo WHERE Task = ? AND Time_in_Hours = ?", (task, time))
    conn.commit()  # Committing the changes to the database
    conn.close()  # Closing the connection

# Function to edit a task in the 'todo' table
def edit_task(old_task, old_time, new_task, new_time):
    conn = connect_db()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object

    # SQL query to update a task's details in the 'todo' table
    cursor.execute("UPDATE todo SET Task = ?, Time_in_Hours = ? WHERE Task = ? AND Time_in_Hours = ?",
                   (new_task, new_time, old_task, old_time))
    conn.commit()  # Committing the changes to the database
    conn.close()  # Closing the connection

# Function to retrieve all tasks from the 'todo' table
def get_tasks():
    conn = connect_db()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object

    # SQL query to select all tasks from the 'todo' table
    cursor.execute("SELECT * FROM todo")
    tasks = cursor.fetchall()  # Fetching all tasks from the result set
    conn.close()  # Closing the connection
    return tasks  # Returning the retrieved tasks
