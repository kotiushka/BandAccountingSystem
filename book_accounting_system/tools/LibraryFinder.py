from __future__ import annotations

from typing import TYPE_CHECKING

from book_accounting_system.books.Book import Book
from book_accounting_system.enumerations.BookType import BookType
from book_accounting_system.exceptions.library_exceptions import BookNotFoundError, UserNotFoundError
from book_accounting_system.users.User import User

if TYPE_CHECKING:
    from book_accounting_system.Library import Library

class LibraryFinder:
    def __init__(self, library: Library):
        self.library = library

        self.books: dict[str, Book] = library.books
        self.users: dict[int, User] = library.users

    def find_book(self, isbn: str) -> Book | None:
        if not self.books.get(isbn):
            raise BookNotFoundError()

        return self.books.get(isbn)

    def find_available_by_type(self, book_type: BookType) -> dict[str, Book]:
        result = {}
        for _, book in self.books.items():
            if book.is_available and book_type is None or book.type == book_type:
                result[book.isbn] = book

        return result

    def find_user(self, u_id: int) -> User | None:
        if not self.users.get(u_id):
            raise UserNotFoundError()

        return self.users.get(u_id)
