import sys
import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "inventory_db"
}



def create_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        return conn
    except Error as e:
        print("Error connecting to database:", e)
        return None


def add_item():
    name = input("Enter item name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        price = float(input("Enter price (e.g., 49.99): ").strip())
        quantity = int(input("Enter quantity (e.g., 10): ").strip())
    except ValueError:
        print("Invalid price or quantity. Try again.")
        return

    conn = create_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)",
                       (name, price, quantity))
        conn.commit()
        print("Item added successfully with id:", cursor.lastrowid)
    except Error as e:
        print("Failed to add item:", e)
    finally:
        cursor.close()
        conn.close()


def view_items():
    conn = create_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, quantity FROM items")
        rows = cursor.fetchall()
        if not rows:
            print("Inventory is empty.")
            return
        print("\n--- Inventory ---")
        print(f"{'ID':<4} {'Name':<25} {'Price':<10} {'Quantity':<8}")
        print("-" * 52)
        for r in rows:
            print(f"{r[0]:<4} {r[1]:<25} {r[2]:<10} {r[3]:<8}")
        print("-" * 52 + "\n")
    except Error as e:
        print("Failed to fetch items:", e)
    finally:
        cursor.close()
        conn.close()


def update_item():
    try:
        item_id = int(input("Enter item ID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    conn = create_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, quantity FROM items WHERE id = %s", (item_id,))
        row = cursor.fetchone()
        if not row:
            print("Item not found.")
            return
        print("Current:", row)
        choice = input("Update (p)rice or (q)uantity or (b)oth ? [p/q/b]: ").strip().lower()
        if choice == "p" or choice == "b":
            try:
                new_price = float(input("Enter new price: ").strip())
                cursor.execute("UPDATE items SET price = %s WHERE id = %s", (new_price, item_id))
            except ValueError:
                print("Invalid price input. Skipping price update.")
        if choice == "q" or choice == "b":
            try:
                new_qty = int(input("Enter new quantity: ").strip())
                cursor.execute("UPDATE items SET quantity = %s WHERE id = %s", (new_qty, item_id))
            except ValueError:
                print("Invalid quantity input. Skipping quantity update.")

        conn.commit()
        print("Item updated successfully.")
    except Error as e:
        print("Failed to update item:", e)
    finally:
        cursor.close()
        conn.close()


def delete_item():
    try:
        item_id = int(input("Enter item ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    confirm = input("Are you sure you want to delete this item? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete canceled.")
        return
    conn = create_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        conn.commit()
        if cursor.rowcount:
            print("Item deleted successfully.")
        else:
            print("Item not found.")
    except Error as e:
        print("Failed to delete item:", e)
    finally:
        cursor.close()
        conn.close()


def main_menu():
    while True:
        print("""
Mini Inventory Management System
--------------------------------
1. Add new item
2. View all items
3. Update item (price/quantity)
4. Delete item
5. Exit
""")
        choice = input("Choose an option [1-5]: ").strip()
        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    print("Make sure MySQL server is running and setup.sql has been executed (to create DB & table).")
    main_menu()
    
