
import sys
import os

# Add project root to sys.path so imports work even if running directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_manager.inventory import LibraryInventory

def print_menu():
    print("\n===== Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    print("=====================================")

def main():
    inventory = LibraryInventory()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(title, author, isbn)
            print("Book added successfully.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_inventory()
                print("Book issued.")
            else:
                print("Book not available or does not exist.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_inventory()
                print("Book returned.")
            else:
                print("Cannot return book or book does not exist.")

        elif choice == "4":
            books = inventory.display_all()
            if not books:
                print("No books in inventory.")
            for b in books:
                print(b)

        elif choice == "5":
            keyword = input("Enter title keyword to search: ")
            results = inventory.search_by_title(keyword)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found with that keyword.")

        elif choice == "6":
            print("Exiting Library Inventory Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
