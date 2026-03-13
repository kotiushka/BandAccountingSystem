from book_accounting_system.Library import Library
from book_accounting_system.books.Book import Book
from book_accounting_system.enumerations.MaxBorrowed import MaxBorrowed
from book_accounting_system.enumerations.Permission import Permission
from book_accounting_system.users.User import User

class Librarian(User):

    _MAX_BORROWED: MaxBorrowed = MaxBorrowed.LIBRARIAN

    def __init__(self, u_id: int, name: str, age: int, library: Library, permissions: set[Permission]):
        super().__init__(u_id, name, age, permissions)
        self._library: Library = library

    @property
    def max_borrowed(self) -> MaxBorrowed:
        return self._MAX_BORROWED

    @property
    def library(self) -> Library:
        return self._library

    def add_book(self, book: Book) -> Library:
        return self._library.add_book(self, book)

    def remove_book(self, isbn: str) -> Book:
        return self._library.remove_book(self, isbn)

    def extend_book_term(self, isbn: str, term: int) -> None:
        self._library.extend_book_term(self, isbn, term)
