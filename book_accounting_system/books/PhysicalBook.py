from typing import Self

from book_accounting_system.books.Book import Book
from book_accounting_system.enumerations.BookFormat import BookFormat
from book_accounting_system.enumerations.BookType import BookType


class PhysicalBook(Book):

    _type: BookType = BookType.PHYSICAL_BOOK
    _borrow_duration_days: int = 14

    def __init__(self, title: str, author: str, isbn: str, year: int, description: str,
                 book_format: BookFormat, shelf: int):

        super().__init__(title, author, isbn, year, description, book_format)
        self.shelf: int = shelf

    @property
    def type(self) -> BookType:
        return self._type

    @property
    def borrow_duration_days(self) -> int:
        return self._borrow_duration_days

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(title=data["title"], author=data["author"],
                   isbn=data["isbn"], year=data["year"], description=data["description"],
                   book_format=BookFormat(data["book_format"]), shelf=data["shelf"])

    def __str__(self):
        return super().__str__() + f" shelf: {self.shelf};"
