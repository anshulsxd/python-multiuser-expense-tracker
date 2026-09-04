import os
import sqlite3
from datetime import date

app_dir = os.path.join(os.getenv("APPDATA"), "ExpenseTracker")
os.makedirs(app_dir, exist_ok=True)
DB_PATH = os.path.join(app_dir, "expensesDataBase.db")

def create_table():
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
    )""")

    connect.commit()
    connect.close()

def add_expense(user_id):
    while True:
        title = input("Enter title*: ")
        amount = float(input("Enter amount*: "))
        category = input("Enter category*: ")
        description = input("Enter description: ")
        expense_date = date.today().isoformat()

        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()

        cursor.execute("""
            INSERT INTO expenses
            (user_id, title, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, title, amount, category, description, expense_date)
            )

        connect.commit()
        connect.close()

        print("Expense added successfully!")

        add_more = input("Add another expense (y/n): ")
        add_more = add_more.lower()
        if add_more != "y":
            break

def view_expense(user_id):
    input_date = input("Enter date (YYYY-MM-DD): ")
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()

    cursor.execute("""
        SELECT id, title, amount, category, description, date
        FROM expenses WHERE user_id = ? AND date = ?""", (user_id, input_date)
    )

    expenses = cursor.fetchall()
    connect.close()

    if not expenses:
        print("\nNo expense(s) on that day :)")
        return

    print(f"==========EXPENSES ON {input_date}==========")
    # name.of.thing    price    category     description
    print(f"{'ID':<5}{'TITLE':<20}{'AMOUNT':<12}{'CATEGORY':<18}{'DESCRIPTION':<30}{'DATE'}")
    print()

    for expense in expenses:
        print(f"{expense[0]:<5}{expense[1]:<20}{expense[2]:<12.2f}{expense[3]:<18}{expense[4]:<30}{expense[5]}")
        print("=" * 115)

def delete_expense(user_id):
    exp_id = int(input("Enter expense ID: "))
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()

    cursor.execute(
        "SELECT user_id FROM expenses WHERE id = ?", (exp_id,)
    )
    verify = cursor.fetchone()

    if verify and verify[0] == user_id:
        cursor.execute(
            "DELETE FROM expenses WHERE id = ? AND user_id = ?", (exp_id, user_id)
        )
        connect.commit()
        print("Expense deleted successfully!")
    
    else:
        print("Invalid Expense ID!")

    connect.close()