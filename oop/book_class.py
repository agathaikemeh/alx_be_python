# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        print(f"Book created: {self.title}")

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """String representation of the Book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"














