from functools import wraps
from typing import Callable, Any

from book_accounting_system.enumerations.Permission import Permission
from book_accounting_system.exceptions.library_exceptions import PermissionDeniedError


def require_permission(*required: Permission) -> Callable:
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, user, *args, **kwargs) -> Any:
            missing = [p for p in required if p not in user.permissions]
            if missing:
                raise PermissionDeniedError(f"permission denied for {user.name}: {', '.join(p.name for p in missing)}")
            return method(self, user, *args, **kwargs)
        return wrapper
    return decorator
