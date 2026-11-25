
books = []
# Add book
def add_book():
    bid = input("Enter book ID: ")
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    for b in books:
        if b["id"] == bid:
            print("Book ID already exists")
            return

    book = {
        "id": bid,
        "name": name,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    print("Book added successfully!")


# Display books
def display_books():
    if len(books) == 0:
        print("No books available")
    else:
        for b in books:
            print("--------------------")
            print("Book ID:", b["id"])
            print("Book Name:", b["name"])
            print("Author:", b["author"])
            print("Status:", b["status"])


# Search book
def search_book():
    bid = input("Enter book ID: ")

    for b in books:
        if b["id"] == bid:
            print("Book found!")
            print(b)
            return

    print("Book not found")


# Issue book
def issue_book():
    bid = input("Enter book ID to issue: ")

    for b in books:
        if b["id"] == bid:

            if b["status"] == "Available":
                b["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued")

            return

    print("Book not found")


# Return book
def return_book():
    bid = input("Enter book ID to return: ")

    for b in books:
        if b["id"] == bid:

            if b["status"] == "Issued":
                b["status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available")

            return

    print("Book not found")


# Delete book
def delete_book():
    bid = input("Enter book ID to delete: ")

    for b in books:
        if b["id"] == bid:

            if b["status"] == "Available":
                books.remove(b)
                print("Book deleted successfully!")
            else:
                print("Cannot delete an issued book")

            return

    print("Book not found")


# Main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

