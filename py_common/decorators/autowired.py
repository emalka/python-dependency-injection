import inspect
from enum import Enum
from functools import wraps


class AutoWiredType(Enum):
    SINGLETON = 'singleton'
    SINGLECALL = 'singlecall'


def autowired(auto_wired_type: AutoWiredType=AutoWiredType.SINGLETON):
    """
        Notice: currently does not support nested locking beware will result in a deadlock
    """
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            signature: inspect.Signature = inspect.signature(func)
            parameter: inspect.Parameter = None
            annotation: type = None

            for key in signature.parameters:
                parameter = signature.parameters[key]
                annotation = parameter.annotation

                if key == 'self':
                    pass

                elif annotation == inspect._empty:
                    pass

                else:
                    if auto_wired_type == AutoWiredType.SINGLETON:
                        obj = parameter.annotation()
                    elif auto_wired_type == AutoWiredType.SINGLECALL:
                        obj = parameter.annotation()

            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper
