import copy
from typing import Self

from book_accounting_system.books.Book import Book
from book_accounting_system.enumerations.BookType import BookType
from book_accounting_system.enumerations.Permission import Permission
from book_accounting_system.exceptions.library_exceptions import BookNotFoundError, \
    BookAvailabilityError, BookAlreadyExistsError, UserAlreadyExistsError, UserNotFoundError
from book_accounting_system.tools.LibraryFinder import LibraryFinder
from book_accounting_system.tools.decorators import require_permission
from book_accounting_system.users.User import User


class Library:
    def __init__(self, name: str, books: dict[str, Book]):
        self.name: str = name
        self._books: dict[str, Book] = copy.deepcopy(books)

        self._users: dict[int, User] = {}

        self.library_finder: LibraryFinder = LibraryFinder(self)

    @property
    def books(self) -> dict[str, Book]:
        return copy.deepcopy(self._books)

    @property
    def users(self) -> dict[int, User]:
        return self._users

    @require_permission(Permission.BORROW_BOOK)
    def borrow_book(self, _user: User, isbn: str) -> None:
        book = self.library_finder.find_book(isbn)

        if not book.is_available:
            raise BookAvailabilityError("the book is unavailable")

        book.borrow()

    @require_permission(Permission.RETURN_BOOK)
    def return_book(self, _user: User, isbn: str) -> None:
        book = self.library_finder.find_book(isbn)

        if book.is_available:
            raise BookAvailabilityError("the book is already available")

        book.b_return()

    @require_permission(Permission.ADD_BOOK)
    def add_book(self, _user: User, book: Book) -> Self:
        try:
            self.library_finder.find_book(book.isbn)
            raise BookAlreadyExistsError()
        except BookNotFoundError:
            self._books[book.isbn] = book
            return self

    @require_permission(Permission.REMOVE_BOOK)
    def remove_book(self, _user: User, isbn: str) -> Book:
        self.library_finder.find_book(isbn)
        return self._books.pop(isbn)

    @require_permission(Permission.EXTEND_BOOK_TERM)
    def extend_book_term(self, _user: User, isbn: str, term: int) -> Self:
        self.library_finder.find_book(isbn)

        self._books[isbn].borrow_duration_days = term
        return self

    @require_permission(Permission.SEARCH_BOOK)
    def list_available_books(self, _user: User, book_type: BookType=None) -> dict[str, Book]:
        return self.library_finder.find_available_by_type(book_type)

    @require_permission(Permission.MANAGE_USERS)
    def _add_user(self, _user_obj: User, user: User) -> Self:
        try:
            self.library_finder.find_user(user.u_id)
            raise UserAlreadyExistsError()
        except UserNotFoundError:
            self._users[user.u_id] = user
            return self

    @require_permission(Permission.MANAGE_USERS)
    def _remove_user(self, _user_obj: User,u_id: int) -> User:
        self.library_finder.find_user(u_id)
        return self._users.pop(u_id)

    def __len__(self) -> int:
        return len(self._books)
