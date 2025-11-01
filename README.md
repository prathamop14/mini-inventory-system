# Mini Inventory Management System

A simple console-based Inventory Management System using **Python** and **MySQL**.
This project demonstrates basic **CRUD operations** (Create, Read, Update, Delete) and is suitable for beginners to showcase on GitHub.

## Features
- Add new item (name, price, quantity)
- View all items in inventory
- Update item price or quantity
- Delete an item

## Technologies
- Python 3.x
- MySQL
- mysql-connector-python (Python package)

## Setup Instructions

1. **Install Python 3** (if not installed): https://www.python.org/downloads/

2. **Install MySQL** and make sure the server is running.
   - Default username used in the code: `root`
   - Default password used in the code: (empty)
   - If your MySQL uses a different username/password, update the `DB_CONFIG` in `inventory.py` accordingly.

3. **Install Python package**:
```bash
pip install mysql-connector-python
```

4. **Create database and table**:
- Open your MySQL client (or MySQL Workbench) and run the SQL commands from `setup.sql`:
```bash
mysql -u root < setup.sql
```
(Or copy-paste the commands inside `setup.sql` into your MySQL client.)

5. **Run the program**:
```bash
python inventory.py
```

6. **Usage**:
- Choose options from the menu to add, view, update, or delete items.
- If you change your MySQL username/password, update `DB_CONFIG` in `inventory.py` before running.

## How to upload to GitHub
1. Create a new repository on GitHub (e.g., `mini-inventory-system`).
2. Upload these three files: `inventory.py`, `setup.sql`, `README.md`.
3. Add a short README description (the file here is ready to use).

## Notes for interviews
- Explain that this is a beginner-level console project showing CRUD operations and database connectivity.
- Mention you wrote the Python script to interact with a MySQL database using `mysql-connector-python`.
- Keep explanations simple: how you insert/select/update/delete records and how the menu works.

---
Good luck! If you want, I can also format the project into a ZIP so you can download and upload to GitHub directly.