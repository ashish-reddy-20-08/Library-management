import json
import logging
from .storage import Storage

# defining class book below with default methods
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "available": self.available}

    @staticmethod
    def from_dict(data):
        book = Book(data['title'], data['author'], data['isbn'])
        book.available = data['available']
        return book

# book manager with the functions like add, search, delete ...
class BookManager:
    def __init__(self, storage_file='books.json'):
        self.storage = Storage(storage_file)
        self.books = self.load_books()

    def load_books(self):
        return [Book.from_dict(book) for book in self.storage.load()]

    def save_books(self):
        self.storage.save([book.to_dict() for book in self.books])

    def add_book(self, title, author, isbn):
        if self.search_books(isbn=isbn):
            logging.warning("Book with this ISBN already exists.")
            print("Book with this ISBN already exists.")
            return
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        logging.info(f"Book added: {title} by {author} (ISBN: {isbn})")
        print("Book added.")

    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                logging.info(f"Book updated: {isbn}")
                print("Book updated.")
                return
        logging.warning(f"Book not found: {isbn}")
        print("Book not found.")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                logging.info(f"Book deleted: {isbn}")
                print("Book deleted.")
                return
        logging.warning(f"Book not found: {isbn}")
        print("Book not found.")

    def list_books(self):
        for book in self.books:
            print(book.to_dict())

    def search_books(self, **kwargs):
        results = []
        for book in self.books:
            if all(getattr(book, k) == v for k, v in kwargs.items()):
                results.append(book)
        if not results:
            logging.info("No books found.")
            print("No books found.")
        return results

    def print_search_results(self, results):
        for book in results:
            print(book.to_dict())
