📚 Library Inventory Manager

Course: Programming for Problem Solving using Python
Assignment: Mini Project – Library Management System
Author: Harshit Kumar Singh
Date: 01-12-2025

📝 Project Overview

This project implements a lightweight command-line Library Inventory System using Object-Oriented Programming, JSON file handling, logging, and exception management.
The system allows library staff to:

~Add books
~Issue and return books
~Search by title or ISBN
~View all available books
~Maintain persistent data storage

🏗️ Project Structure
library_inventory_manager/
│
├── cli/
│   └── main.py
│
├── library_manager/
│   ├── book.py
│   ├── inventory.py
│   └── __init__.py
│
├── data/
│   └── books.json
│
├── tests/
│   ├── test_inventory.py
│   └── __init__.py
│
├── logs/
│   └── library.log
│
├── README.md
├── requirements.txt
└── .gitignore

▶️ How to Run the Program

1. Open a terminal inside the project folder
2. Run the CLI:
python cli/main.py

🔧 Features

Add new books with title, author, and ISBN
Issue and return books
Search books by title or ISBN
Persistent storage using JSON
Robust exception handling
Logging with INFO and ERROR levels
Bonus: unit tests using pytest/unittest

🧪 Running Tests

From the project directory:
pytest
or
python -m unittest

📁 Data File

All book data is saved in:
data/catalog.json

THANK YOU !!
