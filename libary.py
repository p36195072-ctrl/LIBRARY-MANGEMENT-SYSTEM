import json

# Load data
try:
    with open("lib.json", "r") as file:
        lib = json.load(file)
except FileNotFoundError:
    lib = {}

def addbook():
    book = input("Enter the book name: ")

    if book == "":
        print("Book name can't be empty")
        return

    lib[book] = {
        "book name": book
    }

    print("Book added successfully!")

def viewbook():
    book = input("Enter the name of the book: ")

    if book == "":
        print("Book name can't be empty")
        return

    if book in lib:
        print("\nBook Found")
        print("Book Name:", lib[book]["book name"])
    else:
        print("Book not found.")

while True:
    print("\nLIBRARY")
    print("1. Add Book")
    print("2. View Book")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addbook()

    elif choice == "2":
        viewbook()

    elif choice == "3":
        with open("lib.json", "w") as file:
            json.dump(lib, file, indent=4)

        print("Total Books =", len(lib))
        print("Exiting...")
        break

    else:
        print("Invalid choice!")