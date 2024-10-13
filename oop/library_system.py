# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        """Initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        """Return string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook attributes, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        """Return string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

