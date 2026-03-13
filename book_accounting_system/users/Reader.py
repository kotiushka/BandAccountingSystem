from book_accounting_system.enumerations.MaxBorrowed import MaxBorrowed
from book_accounting_system.users.User import User


class Reader(User):

    _MAX_BORROWED: MaxBorrowed = MaxBorrowed.READER

    @property
    def max_borrowed(self) -> MaxBorrowed:
        return self._MAX_BORROWED
