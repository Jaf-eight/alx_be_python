"""Library system demonstrating inheritance (Book -> EBook, PrintBook)
and composition (Library managing a collection of books).
"""
from typing import List

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int) -> None:
        # Call base class initializer for common attributes
        super().__init__(title, author)
        # Unique attribute for EBook
        self.file_size = file_size  # in KB

class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int) -> None:
        # Call base class initializer for common attributes
        super().__init__(title, author)
        # Unique attribute for PrintBook
        self.page_count = page_count

class Library:
    """Composition: Library contains a collection of books."""
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self) -> None:
        """Print details of each book in the library.
        Shows common attributes for Book and specific ones for EBook/PrintBook.
        """
        for b in self.books:
            if isinstance(b, EBook):
                print(f"EBook: {b.title} by {b.author}, File Size: {b.file_size}KB")
            elif isinstance(b, PrintBook):
                print(f"PrintBook: {b.title} by {b.author}, Page Count: {b.page_count}")
            else:
                print(f"Book: {b.title} by {b.author}")
