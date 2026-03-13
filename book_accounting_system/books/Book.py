from abc import ABC, abstractmethod
from typing import Self

from book_accounting_system.enumerations.BookFormat import BookFormat
from book_accounting_system.enumerations.BookType import BookType
from descriptors.CorrectISBN import CorrectISBN
from descriptors.CorrectYear import CorrectYear


class Book(ABC):
    _type: BookType = BookType.PHYSICAL_BOOK
    _borrow_duration_days: int = 90

    isbn = CorrectISBN()
    year = CorrectYear()

    def __init__(self, title: str, author: str, isbn: str, year: int, description: str,
                 book_format: BookFormat, available: bool = True):
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.year: int = year
        self._is_available: bool = available
        self.book_format = book_format

        self.description: str = description

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> Self:
        pass

    @property
    def is_available(self) -> bool:
        return self._is_available

    @property
    @abstractmethod
    def type(self) -> BookType:
        return self._type

    @property
    @abstractmethod
    def borrow_duration_days(self) -> int:
        return self._borrow_duration_days

    @borrow_duration_days.setter
    def borrow_duration_days(self, duration: int):
        if not 0 < duration < 90:
            raise ValueError("incorrect borrow duration days provided")

        self._borrow_duration_days = duration

    def borrow(self) -> Self:
        if self._is_available:
            self._is_available = False
            return self

        return self

    def b_return(self) -> Self:
        if not self._is_available:
            self._is_available = True
            return self

        return self

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        return len(isbn) == 13

    def __str__(self) -> str:
        return (
            f"{self.book_format} \"{self.title}\" by {self.author}\n"
            f"ISBN: {self.isbn}  |  Year: {self.year}\n"
            f"Available: {'Yes' if self._is_available else 'No'}  "
            f"Borrow duration: {self._borrow_duration_days} days\n"
            f"Description: {self.description}"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"title={self.title!r}, "
            f"author={self.author!r}, "
            f"isbn={self.isbn!r}, "
            f"year={self.year!r}, "
            f"description={self.description!r}, "
            f"_is_available={self._is_available!r}, "
            f"_borrow_duration_days={self._borrow_duration_days!r}, "
            f"_format={self.book_format!r}"
        )

