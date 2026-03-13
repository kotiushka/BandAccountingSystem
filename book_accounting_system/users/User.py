from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from book_accounting_system.enumerations.MaxBorrowed import MaxBorrowed
from book_accounting_system.enumerations.Permission import Permission
from book_accounting_system.exceptions.library_exceptions import BorrowLimitExceededError

if TYPE_CHECKING:
    from book_accounting_system.Library import Library

class User(ABC):
    _MAX_BORROWED: MaxBorrowed = MaxBorrowed.READER

    def __init__(self, u_id: int, name: str, age: int, permissions: set[Permission]):
        self._u_id = u_id
        self.name: str = name
        self.age: int = age

        self._PERMISSIONS = permissions

        self._borrowed_books: list[str] = []

    @property
    @abstractmethod
    def max_borrowed(self) -> MaxBorrowed:
        return self._MAX_BORROWED

    @property
    def permissions(self) -> set[Permission]:
        return self._PERMISSIONS

    @property
    def borrowed_books(self) -> list[str]:
        return self._borrowed_books

    @property
    def u_id(self) -> int:
        return self._u_id

    def borrow(self, library: Library, isbn: str) -> None:
        if len(self._borrowed_books) < self._MAX_BORROWED:
            library.borrow_book(isbn)
            self._borrowed_books.append(isbn)
            return

        raise BorrowLimitExceededError("it is impossible to issue the book")

    def return_book(self, library: Library, isbn: str) -> None:
        library.return_book(isbn)
        self._borrowed_books.remove(isbn)

    def __str__(self) -> str:
        return f"library user: {self.name}\n; borrowed books: {self._borrowed_books}\n"
