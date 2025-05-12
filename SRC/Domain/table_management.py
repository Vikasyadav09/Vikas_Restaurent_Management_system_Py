import json
import os
from datetime import datetime

TABLE_FILE = r'D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\table.json'

def load_tables():
        
        with open(TABLE_FILE, 'r') as f:
            tables = json.load(f)
        return tables

def save_tables(tables):
    with open(TABLE_FILE, 'w') as f:
        json.dump(tables, f, indent=2)

def show_tables(tables):
    print("\nAll Tables:")
    for t in tables:
        status = "Booked" if t["is_booked"] else "Available"
        booked_time = f" (at {t['booked_at']})" if t["is_booked"] else ""
        print(f"Table No and Total Seat {t['table_no'], t['seat']}: {status}{booked_time}")

def get_available_tables(tables):
    return [t for t in tables if not t["is_booked"]]

def book_table():
    tables = load_tables()
    show_tables(tables)

    available_tables = get_available_tables(tables)
    if not available_tables:
        print("Sorry, no tables are available.")
        return

    print("\nAvailable tables:", [t["table_no"] for t in available_tables])
    try:
        table_choice = int(input("Enter table number you want to book: "))
        selected_table = next((t for t in tables if t["table_no"] == table_choice), None)
        if selected_table and not selected_table["is_booked"]:
            selected_table["is_booked"] = True
            selected_table["booked_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tables(tables)
            print(f"Table {table_choice} booked successfully at {selected_table['booked_at']}!")
        else:
            print("Invalid or already booked table.")
    except ValueError:
        print("Please enter a valid table number.")

    # Show updated table status
    updated_tables = load_tables()
    print("\nUpdated Available Tables:", [t["table_no"] for t in get_available_tables(updated_tables)])

book_table()
