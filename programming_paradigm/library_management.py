# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book is already checked out
    
    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that holds a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found
    
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")


