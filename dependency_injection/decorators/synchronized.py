from functools import wraps
from threading import Lock
mutex: Lock = Lock()


def synchronized():
    """
        Notice: currently does not support nested locking beware will result in a deadlock
    """
    def wrapper(f):
        @wraps(f)
        def inner_wrapper(*args, **kwargs):
            lock: Lock = mutex

            # Try to use the calling class lock if it exist
            try:
                if args[0].lock:
                    lock = args[0].lock
            except Exception as ex:
                pass

            with lock:
                return f(*args, **kwargs)
        return inner_wrapper
    return wrapper
