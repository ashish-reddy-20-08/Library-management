# Import all the required modules
import logging
from library.book import BookManager
from library.user import UserManager
from library.checkout import CheckoutManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# declaration of the main menu
def main_menu():
    print("\n<=================================================>")
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout Book")
    print("4. Checkin Book")
    print("5. List All Books with Status")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

# declaration of the book menu which will be inside the main menu 
def book_menu():
    print("\n<=================================================>")
    print("\nBook Management")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Books")
    print("6. Return to Main Menu")
    choice = input("Enter choice: ")
    return choice

# declaration of the user menu which will be inside the main menu
def user_menu():
    print("\n<=================================================>")
    print("\nUser Management")
    print("1. Add User")
    print("2. List Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Search Users")
    print("6. Return to Main Menu")
    choice = input("Enter choice: ")
    return choice

# list of conditions are written below
def main():
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager(book_manager, user_manager)

    while True:
        choice = main_menu()
        if choice == '1':
            while True:
                b_choice = book_menu()
                if b_choice == '1':
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    isbn = input("Enter ISBN: ")
                    book_manager.add_book(title, author, isbn)
                elif b_choice == '2':
                    book_manager.list_books()
                elif b_choice == '3':
                    isbn = input("Enter ISBN of the book to update: ")
                    title = input("Enter new title (leave blank to keep unchanged): ")
                    author = input("Enter new author (leave blank to keep unchanged): ")
                    book_manager.update_book(isbn, title or None, author or None)
                elif b_choice == '4':
                    isbn = input("Enter ISBN of the book to delete: ")
                    book_manager.delete_book(isbn)
                elif b_choice == '5':
                    attribute = input("Search by (title/author/isbn): ").lower()
                    value = input(f"Enter {attribute}: ")
                    results = book_manager.search_books(**{attribute: value})
                    book_manager.print_search_results(results)
                elif b_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '2':
            while True:
                u_choice = user_menu()
                if u_choice == '1':
                    name = input("Enter user name: ")
                    user_id = input("Enter user ID: ")
                    user_manager.add_user(name, user_id)
                elif u_choice == '2':
                    user_manager.list_users()
                elif u_choice == '3':
                    user_id = input("Enter user ID of the user to update: ")
                    name = input("Enter new name (leave blank to keep unchanged): ")
                    user_manager.update_user(user_id, name or None)
                elif u_choice == '4':
                    user_id = input("Enter user ID of the user to delete: ")
                    user_manager.delete_user(user_id)
                elif u_choice == '5':
                    attribute = input("Search by (name/user_id): ").lower()
                    value = input(f"Enter {attribute}: ")
                    results = user_manager.search_users(**{attribute: value})
                    user_manager.print_search_results(results)
                elif u_choice == '6':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(isbn)
        elif choice == '5':
            checkout_manager.list_books_with_status()
        elif choice == '6':
            logging.info("Exiting the system.")
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
