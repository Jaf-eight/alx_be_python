
class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

class PrintBook(Book):
    def __init__(self, title, author, year, page_count, publisher=None):
        super().__init__(title, author, year)
        self.page_count = int(page_count)
        self.publisher = publisher if publisher is not None else ""

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.page_count} pages"

    def __repr__(self):
        return (
            f"PrintBook('{self.title}', '{self.author}', {self.year}, {self.page_count}, "
            f"{repr(self.publisher)})"
        )

class EBook(Book):
    def __init__(self, title, author, year, file_size_mb, format_):
        super().__init__(title, author, year)
        self.file_size_mb = float(file_size_mb)
        self.format_ = str(format_)

    def __str__(self):
        base = super().__str__()
        return f"{base} | {self.file_size_mb} MB ({self.format_})"

    def __repr__(self):
        return (
            f"EBook('{self.title}', '{self.author}', {self.year}, "
            f"{self.file_size_mb}, '{self.format_}')"
        )

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(b) for b in self.books]
