library = {}
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    library[book_id] = title
    print(f"Book '{title}' added.")

def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in library:
        removed = library.pop(book_id)
        print(f"Book '{removed}' removed.")
    else:
        print("Book ID not found!")

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        print(f"Book ID {book_id} → Title: {library[book_id]}")
    else:
        print("Book ID not found!")

def update_book():
    book_id = input("Enter Book ID to update: ")
    if book_id in library:
        new_title = input("Enter new title: ")
        library[book_id] = new_title
        print(f"Book ID {book_id} updated to '{new_title}'.")
    else:
        print("Book ID not found!")

def display_books():
    if library:
        print("All books:")
        for book_id, title in library.items():
            print(f"ID: {book_id} → Title: {title}")
    else:
        print("Library is empty!")

def count_books():
    print(f"Total books: {len(library)}")

def check_title():
    title = input("Enter title to check: ")
    if title in library.values():
        print(f"Book '{title}' exists in the library.")
    else:
        print(f"Book '{title}' does NOT exist.")

# --- Menu ---
while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Total Books")
    print("7. Check Book Title Exists")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        count_books()
    elif choice == "7":
        check_title()
    elif choice == "8":
        print("Exiting library system.")
        break
    else:
        print("Invalid choice! Please enter 1-8.")
