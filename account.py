import os
import sqlite3
import hashlib

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenseDataBase.db") # finds path (in which folder) of main.py and adds .db file at last of path

def create_table():
    connect = sqlite3.connect(DB_PATH) # creats db file
    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connect.commit()
    connect.close()

class CreateAcc:
    def signup(self):
        username = input("Create username: ")
        password = input("Create password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()

        try:
            cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password)
            )
            connect.commit()
            print("User created successfully!")
        except sqlite3.IntegrityError:
            print("User already exits!")

        connect.close()

class Login:
    def signin(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE username=? AND password=?", (username, hashed_password)
        )
        user = cursor.fetchone()
        connect.close()

        if user:
            print("Login successful!")
            return user[0]
        else:
            print("Invalid username or password!")
            return None

class DeleteAcc:
    def deleteacc(self, user_id):
        password = input("Enter your account password: ")
        password = hashlib.sha256(password.encode()).hexdigest()

        connect = sqlite3.connect(DB_PATH)
        cursor = connect.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE id = ?", (user_id,)
        )

        user_pass = cursor.fetchone()
        connect.close()

        if user_pass and user_pass[0] == password:
            confirm = input("Are you sure, you want to DELETE YOUR ACCOUNT? (y/n): ")
            confirm = confirm.lower()
            if confirm == "y":
                connect = sqlite3.connect(DB_PATH)
                cursor = connect.cursor()

                cursor.execute(
                    "DELETE FROM expenses WHERE user_id = ?", (user_id,)
                )

                cursor.execute(
                    "DELETE FROM users WHERE id = ?", (user_id,)
                )

                connect.commit()
                connect.close()

                print("Your account have been deleted successfully!")
                return True

            else:
                print("Okay! Cancelled.")
                return False

        else:
            print("Incorrect passsword! Try again...")
            return False