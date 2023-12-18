from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, availability_status=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = availability_status

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability Status: {'Available' if self.availability_status else 'Not Available'}")

    def update_availability_status(self, new_status):
        self.availability_status = new_status
        print(f"Availability Status updated to {'Available' if new_status else 'Not Available'}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Books Borrowed: {', '.join(self.books_borrowed)}" if self.books_borrowed else "No books borrowed")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book.title)
            book.update_availability_status(False)
            print(f"{self.name} has borrowed the book '{book.title}'.")
        else:
            print(f"Sorry, the book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_availability_status(True)
            print(f"{self.name} has returned the book '{book.title}'.")
        else:
            print(f"{self.name}, you haven't borrowed the book '{book.title}'.")


class Transaction:
    def __init__(self, user, book, action):
        self.user = user
        self.book = book
        self.action = action
        self.transaction_date = datetime.now()

    def display_transaction_details(self):
        print(f"Transaction Date: {self.transaction_date}")
        print(f"User: {self.user.name} (User ID: {self.user.user_id})")
        print(f"Book: {self.book.title}")
        print(f"Action: {self.action}")
        print("---")


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered with user ID: {user.user_id}.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(f"  - {book.title}")

    def display_users(self):
        if not self.users:
            print("No users registered in the library.")
        else:
            print("Users registered in the library:")
            for user in self.users:
                print(f"  - {user.name} (User ID: {user.user_id})")

    def handle_transaction(self, user_id, book_title, action):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book:
            if action == "borrow":
                user.borrow_book(book)
            elif action == "return":
                user.return_book(book)
            else:
                print("Invalid action. Use 'borrow' or 'return'.")

            transaction = Transaction(user, book, action)
            self.transactions.append(transaction)

        else:
            print("User or book not found.")

    def generate_transaction_report(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("Transaction Report:")
            for transaction in self.transactions:
                transaction.display_transaction_details()


def print_user_menu():
    print("\nUser Menu:")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Display Available Books")
    print("4. Display User Details")
    print("5. Exit")


def print_librarian_menu():
    print("\nLibrarian Menu:")
    print("1. Add Book")
    print("2. Register User")
    print("3. Display Available Books")
    print("4. Display Registered Users")
    print("5. Generate Transaction Report")
    print("6. Exit")


def main():
    library = Library()

    while True:
        user_type = input("Are you a User or a Librarian? (Type 'user' or 'librarian', or 'exit' to quit): ").lower()

        if user_type == 'exit':
            print("Exiting the Library Management System. Goodbye!")
            break

        elif user_type == 'user':
            user_id = int(input("Enter your user ID: "))
            current_user = next((u for u in library.users if u.user_id == user_id), None)

            if current_user:
                while True:
                    print_user_menu()
                    user_choice = input("Enter your choice (1-5): ")

                    if user_choice == "1":
                        book_title = input("Enter the book title to borrow: ")
                        library.handle_transaction(user_id, book_title, "borrow")

                    elif user_choice == "2":
                        book_title = input("Enter the book title to return: ")
                        library.handle_transaction(user_id, book_title, "return")

                    elif user_choice == "3":
                        library.display_books()

                    elif user_choice == "4":
                        current_user.display_details()

                    elif user_choice == "5":
                        print("Exiting the User Menu.")
                        break

                    else:
                        print("Invalid choice. Please enter a number from 1 to 5.")

            else:
                print("User not found. Please register or try again.")

        elif user_type == 'librarian':
            while True:
                print_librarian_menu()
                librarian_choice = input("Enter your choice (1-6): ")

                if librarian_choice == "1":
                    title = input("Enter the book title: ")
                    author = input("Enter the author: ")
                    isbn = input("Enter the ISBN: ")
                    new_book = Book(title, author, isbn)
                    library.add_book(new_book)

                elif librarian_choice == "2":
                    name = input("Enter the user's name: ")
                    new_user = User(len(library.users) + 1, name)
                    library.register_user(new_user)

                elif librarian_choice == "3":
                    library.display_books()

                elif librarian_choice == "4":
                    library.display_users()

                elif librarian_choice == "5":
                    library.generate_transaction_report()

                elif librarian_choice == "6":
                    print("Exiting the Librarian Menu.")
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")

        else:
            print("Invalid choice. Please type 'user', 'librarian', or 'exit'.")


if __name__ == "__main__":
    main()
