from enum import StrEnum, auto
from typing import Self


class Permission(StrEnum):
    BORROW_BOOK = auto()
    RETURN_BOOK = auto()

    SEARCH_BOOK = auto()
    ADD_BOOK = auto()
    REMOVE_BOOK = auto()
    EXTEND_BOOK_TERM = auto()

    MANAGE_USERS = auto()

    @classmethod
    def reader_permissions(cls) -> set[Self]:
        return {cls.BORROW_BOOK, cls.RETURN_BOOK}

    @classmethod
    def librarian_permissions(cls) -> set[Self]:
        return cls.reader_permissions() | {cls.SEARCH_BOOK, cls.ADD_BOOK, cls.REMOVE_BOOK, cls.EXTEND_BOOK_TERM}

    @classmethod
    def admin_permissions(cls) -> set[Self]:
        return cls.reader_permissions() | cls.librarian_permissions() | {cls.MANAGE_USERS}
