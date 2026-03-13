from typing import Self

from book_accounting_system.books.Book import Book
from book_accounting_system.enumerations.BookFormat import BookFormat
from book_accounting_system.enumerations.BookType import BookType


class AudioBook(Book):

    _type: BookType = BookType.AUDIO_BOOK
    _borrow_duration_days: int = 21

    def __init__(self, title: str, author: str, isbn: str, year: int, description: str,
                 book_format: BookFormat, duration_minutes: int, narrator: str):
        super().__init__(title, author, isbn, year, description, book_format)

        self.duration_minutes = duration_minutes
        self.narrator = narrator

    @property
    def type(self) -> BookType:
        return self._type

    @property
    def borrow_duration_days(self) -> int:
        return self._borrow_duration_days

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        pass

    def __str__(self):
        return super().__str__() + f" duration_minutes: {self.duration_minutes}; narrator: {self.narrator};"
