import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)

# Save tasks to file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete task
def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete!")
    else:
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")

        if confirm:
            listbox.delete(selected[0])
            save_tasks()

# Clear all tasks
def clear_tasks():
    confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
    if confirm:
        listbox.delete(0, tk.END)
        save_tasks()

# UI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

title = tk.Label(root, text="My To-Do List", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Delete Task", width=12, command=delete_task).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Clear All", width=12, command=clear_tasks).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=15)
listbox.pack(pady=20)

# Load saved tasks when app starts
load_tasks()

root.mainloop()