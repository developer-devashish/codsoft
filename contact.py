import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("📒 Contact Book")
root.geometry("900x560")
root.config(bg="#f4f6f9")

# ---------------- CONTACT STORAGE ---------------- #
contacts = []

# ---------------- FUNCTIONS ---------------- #

# Add Contact
def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Name and Phone are required!"
        )
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    update_contact_list()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "✅ Contact Added Successfully!"
    )


# View Contacts
def update_contact_list(search_term=""):

    contact_list.delete(*contact_list.get_children())

    found = False

    for index, contact in enumerate(contacts):

        if (
            search_term.lower() in contact["name"].lower()
            or search_term in contact["phone"]
        ):

            found = True

            contact_list.insert(
                "",
                "end",
                iid=index,
                values=(
                    contact["name"],
                    contact["phone"],
                    contact["email"]
                )
            )

    # Contact Not Found
    if not found and search_term != "":
        not_found_label.config(
            text="❌ Contact Not Found"
        )
    else:
        not_found_label.config(text="")


# Search Contact
def search_contact():

    search_term = search_entry.get()

    if search_term == "":
        messagebox.showwarning(
            "Warning",
            "Please enter something to search!"
        )
        return

    update_contact_list(search_term)


# Select Contact
def select_contact(event):

    selected = contact_list.focus()

    if selected:

        values = contact_list.item(selected, "values")

        index = int(selected)

        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[0])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, values[1])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, values[2])

        address_entry.delete("1.0", tk.END)
        address_entry.insert(
            tk.END,
            contacts[index]["address"]
        )


# Update Contact
def update_contact():

    selected = contact_list.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact to update!"
        )
        return

    index = int(selected)

    contacts[index]["name"] = name_entry.get()
    contacts[index]["phone"] = phone_entry.get()
    contacts[index]["email"] = email_entry.get()
    contacts[index]["address"] = address_entry.get(
        "1.0",
        tk.END
    ).strip()

    update_contact_list()
    clear_fields()

    messagebox.showinfo(
        "Updated",
        "✏️ Contact Updated Successfully!"
    )


# Delete Contact
def delete_contact():

    selected = contact_list.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact to delete!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this contact?"
    )

    if confirm:

        contacts.pop(int(selected))

        update_contact_list()
        clear_fields()

        messagebox.showinfo(
            "Deleted",
            "❌ Contact Deleted Successfully!"
        )


# Clear Fields
def clear_fields():

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)


# ---------------- UI DESIGN ---------------- #

title = tk.Label(
    root,
    text="📒 Contact Book",
    font=("Arial", 26, "bold"),
    bg="#f4f6f9",
    fg="#2c3e50"
)
title.pack(pady=15)

# ---------------- FORM FRAME ---------------- #

form_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief=tk.RIDGE
)
form_frame.pack(
    side=tk.LEFT,
    padx=20,
    pady=10,
    fill=tk.Y
)

# Name
tk.Label(
    form_frame,
    text="Name",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w", padx=10, pady=(10, 0))

name_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)
name_entry.pack(padx=10, pady=5)

# Phone
tk.Label(
    form_frame,
    text="Phone",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w", padx=10)

phone_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)
phone_entry.pack(padx=10, pady=5)

# Email
tk.Label(
    form_frame,
    text="Email",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w", padx=10)

email_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)
email_entry.pack(padx=10, pady=5)

# Address
tk.Label(
    form_frame,
    text="Address",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w", padx=10)

address_entry = tk.Text(
    form_frame,
    width=28,
    height=4,
    font=("Arial", 11)
)
address_entry.pack(padx=10, pady=5)

# ---------------- BUTTONS ---------------- #

btn_frame = tk.Frame(
    form_frame,
    bg="white"
)
btn_frame.pack(pady=15)

# Add Button
add_btn = tk.Button(
    btn_frame,
    text="➕ Add",
    width=12,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_contact
)
add_btn.grid(row=0, column=0, padx=5, pady=5)

# Update Button
update_btn = tk.Button(
    btn_frame,
    text="✏️ Update",
    width=12,
    bg="#3498db",
    fg="white",
    font=("Arial", 11, "bold"),
    command=update_contact
)
update_btn.grid(row=0, column=1, padx=5, pady=5)

# Delete Button
delete_btn = tk.Button(
    btn_frame,
    text="❌ Delete",
    width=12,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 11, "bold"),
    command=delete_contact
)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

# Clear Button
clear_btn = tk.Button(
    btn_frame,
    text="🧹 Clear",
    width=12,
    bg="#95a5a6",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear_fields
)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

# ---------------- RIGHT SIDE ---------------- #

right_frame = tk.Frame(
    root,
    bg="#f4f6f9"
)
right_frame.pack(
    side=tk.RIGHT,
    fill=tk.BOTH,
    expand=True,
    padx=10
)

# Search Bar
search_frame = tk.Frame(
    right_frame,
    bg="#f4f6f9"
)
search_frame.pack(fill=tk.X, pady=10)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    width=30
)
search_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(
    search_frame,
    text="🔍 Search",
    bg="#8e44ad",
    fg="white",
    font=("Arial", 11, "bold"),
    command=search_contact
)
search_btn.pack(side=tk.LEFT, padx=5)

show_all_btn = tk.Button(
    search_frame,
    text="📋 Show All",
    bg="#34495e",
    fg="white",
    font=("Arial", 11, "bold"),
    command=lambda: update_contact_list("")
)
show_all_btn.pack(side=tk.LEFT, padx=5)

# Not Found Label
not_found_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9",
    fg="red"
)
not_found_label.pack()

# ---------------- CONTACT LIST ---------------- #

columns = (
    "Name",
    "Phone",
    "Email"
)

contact_list = ttk.Treeview(
    right_frame,
    columns=columns,
    show="headings",
    height=18
)

for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=180)

contact_list.pack(
    fill=tk.BOTH,
    expand=True
)

# Select Event
contact_list.bind(
    "<<TreeviewSelect>>",
    select_contact
)

# ---------------- RUN APP ---------------- #

root.mainloop()