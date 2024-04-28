from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        ...


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class WebFormatter(BaseFormatter):
    def format(self, book: Book):
        return f'{book.author}, {book.title}, {book.content[:5]}'


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


book = Book('Book 1', 'author 1', 'some text in the book')
printer_1 = Printer(PaperFormatter())
printer_2 = Printer(WebFormatter())
print(printer_2.get_book(book))
print(printer_1.get_book(book))
