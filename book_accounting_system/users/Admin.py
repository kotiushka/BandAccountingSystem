from book_accounting_system.enumerations.MaxBorrowed import MaxBorrowed
from book_accounting_system.users.Librarian import Librarian
from book_accounting_system.users.User import User


class Admin(Librarian):
    _MAX_BORROWED: MaxBorrowed = MaxBorrowed.ADMIN


    def add_user(self, user: User) -> None:
        self.library._add_user(self, user)

    def remove_user(self, u_id: int) -> User:
        return self.library._remove_user(self, u_id)
    