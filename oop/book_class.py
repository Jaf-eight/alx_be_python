
class Book:
    """A simple Book model demonstrating Python magic methods."""

    def __init__(self, title: str, author: str, year: int):
        """Constructor: initialize title, author, and year."""
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __del__(self):
        """Destructor: prints a message when the object is about to be deleted."""
        # Use getattr to be safe in case attributes are partially collected
        title = getattr(self, 'title', '<unknown>')
        print(f"Deleting {title}")

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation that can recreate the object."""
        # Use repr() for strings to ensure proper quoting/escaping
        return f"Book({self.title!r}, {self.author!r}, {self.year})"
