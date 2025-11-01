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
