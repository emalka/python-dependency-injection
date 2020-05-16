import builtins
from functools import wraps

from dependency_injection.decorators.autowired_enums import AutoWiredType
from dependency_injection.decorators.autowired_handler import autowired_handler


def autowired(auto_wired_type=AutoWiredType.SINGLETON):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            return autowired_handler.autowire(func, auto_wired_type, *args, **kwargs)
        return inner_wrapper
    return wrapper
