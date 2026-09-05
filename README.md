# Expense Tracker

A Python-based Expense Tracker that allows users to securely manage accounts, record expenses, and store data using SQLite.

## ⚠️ Important Notice Regarding the `.exe` Release

> **Please read this before downloading the `.exe` file.**

At the moment, the `.exe` version of **ExpenseTracker** available in the GitHub Release may not download or run correctly on some Windows systems. I tried to install my own app `ExpenseTrackerTerminal.exe` via Release and browser and MS Defender keep warning "Virus/Thread detected".

Windows Defender/Microsoft security tools may display a **"Virus detected"** warning and block the download. This appears to be related to the way the application is packaged using **PyInstaller**, which can sometimes cause antivirus software to incorrectly flag PyInstaller-generated executables.

- **Note that, executable file and project source code does not contain any virus and thread or any malicious file or stuff that may harm your device. The project is completely created by me and is safe for your device. If you are uncomfortable to download the `.exe` file, just download/clone the source code and review it if you have any doubt.**

### 🔧 Recommended Solution

After installation, your browser download section may display "Virus detected" with a "Keep file" button. Click that `keep file` button

If you still encounter this issue, please use the **source code** provided in this repository instead of the pre-built `.exe`.

You can download/clone the source code and create the `.exe` yourself on your own device using PyInstaller or a different library.

```bash
pyinstaller --clean --onefile main.py
```

## Features

- User account system
- Password authentication
- Add expenses
- View expenses
- Store data using SQLite
- Retrieve expenses by date
- Multiple users support
- Terminal-based interface

## Technologies Used

- Python
- SQLite
- Git & GitHub

## Installation

1. Clone the repository:

```bash
git clone https://github.com/anshulsxd/python-multiuser-expense-tracker.git
```

1. Move into the project folder:

```bash
cd Expense-Tracker
```

1. Run the program:

```bash
python main.py
```



## Project Structure

```
Expense-Tracker/
│
├── main.py
├── account.py
├── expenses.py
├── expenseDataBase.db
├── README.md
└── .gitignore
```



## Future Plans

- GUI version using C#
- Expense categories



## Author

Anshul
