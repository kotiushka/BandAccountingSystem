from datetime import datetime

from book_accounting_system.exceptions.library_exceptions import InvalidYearError


class CorrectYear:
    
    _MIN_YEAR: int = 1450

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)
    
    def __set__(self, instance, value):
        current_year = datetime.now().year
        max_year = current_year + 2
        if not isinstance(value, int):
            raise InvalidYearError("Year must be an integer") 
        if not (self._MIN_YEAR <= value <= max_year):
            raise InvalidYearError(f"Year must be between {self._MIN_YEAR} and {max_year}")
        
        instance.__dict__[self._name] = value
