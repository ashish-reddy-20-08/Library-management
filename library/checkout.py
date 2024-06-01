import logging
from .storage import Storage

# checkout manager class with basic functions like checkin and checkout linked to storage.

class CheckoutManager:
    def __init__(self, book_manager, user_manager, storage_file='checkouts.json'):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.storage = Storage(storage_file)
        self.checkouts = self.load_checkouts()

    def load_checkouts(self):
        return self.storage.load()

    def save_checkouts(self):
        self.storage.save(self.checkouts)

    def checkout_book(self, user_id, isbn):
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)
        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if user and book and book.available:
            book.available = False
            self.checkouts.append({"user_id": user_id, "isbn": isbn})
            self.book_manager.save_books()
            self.save_checkouts()
            logging.info(f"Book {isbn} checked out to user {user_id}.")
            print(f"Book {isbn} checked out to user {user_id}.")
        else:
            logging.warning("Checkout failed. Book might not be available or user/book not found.")
            print("Checkout failed. Book might not be available or user/book not found.")

    def checkin_book(self, isbn):
        book = next((b for b in self.book_manager.books if b.isbn == isbn), None)
        if book:
            book.available = True
            self.checkouts = [c for c in self.checkouts if c['isbn'] != isbn]
            self.book_manager.save_books()
            self.save_checkouts()
            logging.info(f"Book {isbn} checked in.")
            print(f"Book {isbn} checked in.")
        else:
            logging.warning("Checkin failed. Book not found.")
            print("Checkin failed. Book not found.")

    def list_books_with_status(self):
        for book in self.book_manager.books:
            status = "Checked In" if book.available else "Checked Out"
            logging.info(f"Listing book with status: {book.isbn}, {status}")
            print({**book.to_dict(), "status": status})
