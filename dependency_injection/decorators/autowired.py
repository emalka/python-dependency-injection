import builtins
from functools import wraps
from typing import Dict

from dependency_injection.decorators.autowired_enums import AutoWiredType
from dependency_injection.decorators.autowired_handler import autowired_handler


def autowired(auto_wired_type=AutoWiredType.SINGLETON, qualifiers: Dict=None):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            return autowired_handler.autowire(func, auto_wired_type, qualifiers, *args, **kwargs)
        return inner_wrapper
    return wrapper
