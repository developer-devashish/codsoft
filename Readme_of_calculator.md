# Tkinter Calculator App

A simple and interactive Calculator GUI application built with Python and Tkinter. This project performs basic arithmetic operations with a clean user interface.

---

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Clear button to reset input
* Error handling, such as divide by zero
* User-friendly GUI using Tkinter

---

## Technologies Used

* Python
* Tkinter, the built-in GUI library

---

## Preview

The calculator interface includes:

* Display screen
* Number buttons (0-9)
* Operators (+, -, *, /)
* Equal (=) and Clear (C) buttons

---

## Project Structure

```
codsoft/
│── calculator.py
│── Readme.md
```

---

## How It Works

* The user clicks buttons to form an expression (for example, `7+3`).
* The expression appears on the screen.
* When `=` is pressed:

  * The expression is evaluated using Python.
  * The result shows up instantly.

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/developer-devashish/codsoft
   ```

2. Navigate to the project folder:

   ```bash
   cd codsoft
   ```

3. Run the program:

   ```bash
   python calculator.py
   ```

---

## Note

* This project uses `eval()` for simplicity.
* In production-level applications, avoid using `eval()` because of security risks.

---

## Future Improvements

* Dark mode
* Scientific calculator functions (sin, cos, log)
* Keyboard input support
* History of calculations

---

## Acknowledgment

This project was built to help beginners understand:

* GUI development
* Event handling
* Python basics
