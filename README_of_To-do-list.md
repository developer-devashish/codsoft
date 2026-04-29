# To-Do List App (Python Tkinter)

A simple, beginner-friendly To-Do List GUI application built with Python and Tkinter. This app allows users to add, delete, and manage tasks while keeping data safe with JSON.

---

## Features

* Add new tasks
* Delete selected task with confirmation
* Clear all tasks
* Save tasks automatically using JSON
* Load tasks when the app starts
* Warning messages for better user experience

---

## Tech Stack

* Python 3
* Tkinter (GUI library)
* JSON (for data storage)

---

## Project Structure

```
codsoft
│-- To-do_list.py
│-- tasks.json
│-- README.md
```

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/developer-devashish/codsoft
cd codsoft
```

2. Run the app:

```
python To-do_list.py
```

---

## How It Works

* Tasks are stored in a Listbox (Tkinter widget)
* When you:

  * Add, delete, or clear tasks, data is saved to `tasks.json`
* When the app starts, tasks are loaded from `tasks.json`

---

## Preview

Simple UI with:

* Input field for tasks
* Buttons for actions
* Task list display

---

## Future Improvements

* Mark tasks as completed
* Add due dates
* Dark mode UI
* Categories for tasks
* Cloud sync

---

## Contributing

Feel free to fork this repo and improve the project!

---

## License

This project is open-source and free to use.

---

## Acknowledgment

Built using Python’s built-in GUI library Tkinter.
