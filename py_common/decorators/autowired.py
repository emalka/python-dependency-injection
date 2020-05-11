import inspect
from functools import wraps


def autowired():
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
                if not(key == 'self' or annotation == inspect._empty):
                    obj = parameter.annotation()



            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper
