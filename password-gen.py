import tkinter as tk
from tkinter import messagebox
import random
import string

# ------------------ Functions ------------------ #

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showwarning("Invalid", "Length must be greater than 0")
            return

        if var_only_numbers.get():
            characters = string.digits
        else:
            characters = string.ascii_letters

            if var_numbers.get():
                characters += string.digits
            if var_symbols.get():
                characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showwarning("Invalid", "Enter a valid number")


def copy_password():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied!")
    else:
        messagebox.showwarning("Warning", "No password to copy")


# ------------------ UI Setup ------------------ #

root = tk.Tk()
root.title("Password Generator")
root.geometry("380x350")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# ------------------ Title ------------------ #

tk.Label(root, text="Password Generator",
         font=("Segoe UI", 16, "bold"),
         bg="#1e1e2f", fg="#00ffcc").pack(pady=12)

# ------------------ Length ------------------ #

tk.Label(root, text="Password Length:",
         bg="#1e1e2f", fg="white").pack()

length_entry = tk.Entry(root, bg="#2c2c3e", fg="white",
                        insertbackground="white", justify="center", relief="flat")
length_entry.pack(pady=5, ipadx=5, ipady=4)

# ------------------ Options ------------------ #

var_numbers = tk.IntVar()
var_symbols = tk.IntVar()
var_only_numbers = tk.IntVar()

tk.Checkbutton(root, text="Include Numbers",
               variable=var_numbers, bg="#1e1e2f",
               fg="white", selectcolor="#2c2c3e").pack()

tk.Checkbutton(root, text="Include Symbols",
               variable=var_symbols, bg="#1e1e2f",
               fg="white", selectcolor="#2c2c3e").pack()

tk.Checkbutton(root, text="Only Numbers",
               variable=var_only_numbers, bg="#1e1e2f",
               fg="#ffcc00", selectcolor="#2c2c3e").pack(pady=5)

# ------------------ Buttons ------------------ #

tk.Button(root, text="Generate Password",
          command=generate_password,
          bg="#00ffcc", fg="black",
          relief="flat", padx=10, pady=5).pack(pady=12)

# ------------------ Output ------------------ #

password_entry = tk.Entry(root, width=30,
                          font=("Segoe UI", 12),
                          bg="#2c2c3e", fg="#00ffcc",
                          insertbackground="white",
                          justify="center", relief="flat")
password_entry.pack(pady=5, ipady=5)

tk.Button(root, text="Copy to Clipboard",
          command=copy_password,
          bg="#ff4d6d", fg="white",
          relief="flat", padx=10, pady=5).pack(pady=10)

# ------------------ Run ------------------ #

root.mainloop()