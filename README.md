Library Management System

A beginner-friendly Python project that demonstrates how to build a simple library management system using JSON files and dictionaries.

📌 Description

This project allows users to:

Add books
Search books
Save book records permanently
Load book records automatically
View the total number of books
Exit the application safely

Book records are stored in lib.json, so they remain available even after the program is closed.

🧠 Concepts Used

Python Functions
Dictionaries
JSON Storage
File Handling
json.load()
json.dump()
User Input
Conditional Statements
Loops
Data Persistence

✨ Features

✅ Add Book

✅ Search Book

✅ Automatic JSON Saving

✅ Automatic JSON Loading

✅ Total Book Counter

📂 Files

library_manager.py
lib.json

💻 Stored Information

Each book record contains:

Book Name

Example:

{
    "Python Basics": {
        "book name": "Python Basics"
    },
    "Data Structures": {
        "book name": "Data Structures"
    }
}

▶️ Example Output

LIBRARY

1. Add Book
2. View Book
3. Exit
Enter your choice: 1

Enter the book name: Python Basics

Book added successfully!
Enter your choice: 2

Enter the name of the book: Python Basics

Book Found
Book Name: Python Basics
