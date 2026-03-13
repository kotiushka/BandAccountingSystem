class LibraryError(Exception):
    pass
#
class BookNotFoundError(LibraryError):
    pass

class BorrowLimitExceededError(LibraryError):
    pass

class PermissionDeniedError(LibraryError):
    pass

class BookAlreadyExistsError(LibraryError):
    pass

class BookAvailabilityError(LibraryError):
    pass

class InvalidYearError(LibraryError):
    pass

class InvalidISBNError(LibraryError):
    pass

# --------

class UserNotFoundError(LibraryError):
    pass

class UserAlreadyExistsError(LibraryError):
    pass
