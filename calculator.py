import tkinter as tk


# Function to update the display
def click(value):
    entry.insert(tk.END, value)


# Function to clear the display
def clear():
    entry.delete(0, tk.END)


# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Divide by 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("330x400")

# Entry box (display)
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Run app
root.mainloop()