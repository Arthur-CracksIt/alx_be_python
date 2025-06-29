class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, file_size: {self.file_size}"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, page_count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        return self.books.append(book)
    def list_books(self):
        # list_books = [book for book in self.books]
        # for book in list_books:
        for book in self.books:
            print(book)