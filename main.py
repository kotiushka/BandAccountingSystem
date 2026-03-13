from book_accounting_system.books.EBook import EBook
from book_accounting_system.enumerations.Permission import Permission
from book_accounting_system.users.Admin import Admin
from book_accounting_system.users.Librarian import Librarian
import books
from book_accounting_system.Library import Library

lib = Library("Центральная", books.books)

adam = Admin(0, "Adam", 30, lib, Permission.admin_permissions())

adam.add_user(Librarian(1, "Eve", 25, lib, Permission.librarian_permissions()))

b = EBook("Title", "Author", "aaaaaaaaaaaaa", 2020, "", books.BookFormat.PDF, 5)

adam.add_book(b)



