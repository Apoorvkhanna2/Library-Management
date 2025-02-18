import json

def save_books(books, filename="books.json"):
    with open(filename, "w") as file:
        json.dump(books, file, indent=4)

def load_books(filename="books.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def add_book():
    books = load_books()
    title = input("Enter book title: ")
    author = input("Enter author: ")
    copies = int(input("Enter number of copies: "))
    
    books[title] = {
        "author": author,
        "copies": copies
    }
    
    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    for title, details in books.items():
        print(f"\nTitle: {title}")
        print(f"Author: {details['author']}")
        print(f"Copies Available: {details['copies']}")

def borrow_book():
    books = load_books()
    title = input("Enter book title to borrow: ")
    if title in books and books[title]["copies"] > 0:
        books[title]["copies"] -= 1
        save_books(books)
        print("Book borrowed successfully!")
    else:
        print("Book not available.")

def return_book():
    books = load_books()
    title = input("Enter book title to return: ")
    if title in books:
        books[title]["copies"] += 1
        save_books(books)
        print("Book returned successfully!")
    else:
        print("Book not found in library.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
