from typing import List


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int):
        self.page = page

    def __repr__(self):
        return f"{self.title} - {self.author}"


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
        else:
            print(f"The book {book.title} is already in the library")

    def find_book(self, title):
        try:
            book = next(filter(lambda b: b.title == title, self.books))
        except StopIteration:
            return f"The book {title} is not in the library"
        return book

b1 = Book("Book1", "A1")
b2 = Book("Book2", "A2")
b3 = Book("Book3", "A3")
b4 = Book("Book4", "A4")

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b2)
library.add_book(b4)

print(library.find_book("Book1"))
print(library.find_book("Book2"))
print(library.find_book("Book3"))
print(library.find_book("Book4"))