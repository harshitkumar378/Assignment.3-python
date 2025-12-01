import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, file_path="data/catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_inventory()

    def load_inventory(self):
        try:
            if not self.file_path.exists():
                self.books = []
                return

            with open(self.file_path, "r") as f:
                data = json.load(f)

            self.books = [Book(**book) for book in data]
            logging.info("Inventory loaded successfully.")

        except Exception as e:
            logging.error("Error loading inventory: %s", e)
            self.books = []

    def save_inventory(self):
        try:
            self.file_path.parent.mkdir(exist_ok=True)
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
            logging.info("Inventory saved.")
        except Exception as e:
            logging.error("Save error: %s", e)

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_inventory()
        logging.info("Added book: %s", title)

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books
