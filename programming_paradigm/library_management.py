class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else: return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else: return False
    def is_available(self):
        return not self._is_checked_out
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, books):
        result = self._books.append(books)
        return result
    def list_available_books(self):
        available = [book for book in self._books]
        if not available:
            print("No available books")
        else:
            for book in available:
                print(book)
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title}")
                    return
                else:
                    print("Book wasn't checked out.")
                    return
        print("Book not found.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title}")
                    return
                else:
                    print("Book is already checked out.")
                    return
        print("Book not found.")
