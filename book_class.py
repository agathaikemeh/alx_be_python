# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor method to initialize a book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method to delete the book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
