
class Book:
    def __init__(self, title, author, year=None):
        self.title = str(title)
        self.author = str(author)
        self.year = None if year is None else int(year)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        if self.year is None:
            return f"Book('{self.title}', '{self.author}')"
        return f"Book('{self.title}', '{self.author}', {self.year})"

class PrintBook(Book):
    def __init__(self, title, author, page_count, year=None, publisher=None):
        super().__init__(title, author, year)
        self.page_count = int(page_count)
        self.publisher = publisher if publisher is not None else ""

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        args = [repr(self.title), repr(self.author), str(self.page_count)]
        if self.year is not None:
            args.append(str(self.year))
        if self.publisher:
            args.append(repr(self.publisher))
        return f"PrintBook({', '.join(args)})"

class EBook(Book):
    def __init__(self, title, author, file_size, year=None, format_=None):
        super().__init__(title, author, year)
        self.file_size = int(file_size)
        self.format_ = str(format_) if format_ is not None else ""

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        args = [repr(self.title), repr(self.author), str(self.file_size)]
        if self.year is not None:
            args.append(str(self.year))
        if self.format_:
            args.append(repr(self.format_))
        return f"EBook({', '.join(args)})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(b) for b in self.books]
