from book_accounting_system.exceptions.library_exceptions import InvalidISBNError


class CorrectISBN:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)
    
    def __set__(self, instance, value):
        if not isinstance(value, str) or not len(value) == 13:
            raise InvalidISBNError("ISBN must be a string of 13 characters")
        instance.__dict__[self._name] = value
