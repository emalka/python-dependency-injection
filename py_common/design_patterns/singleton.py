import functools
import threading


def synchronized(lock):
    """ Synchronization decorator """
    def wrapper(f):
        @functools.wraps(f)
        def inner_wrapper(*args, **kw):
            with lock:
                return f(*args, **kw)
        return inner_wrapper
    return wrapper


class Singleton(type):
    """
    Fixme the class doesn't support multiple locks, hence nested singleton objects will have deadlock.
    Fixme Possible solution is to create lock per class
    """

    lock = threading.Lock()
    _instances = {}

    """
    Fixme since nested singleton objects create a deadlock threading synchronization while creating
    Fixme a Singleton is prevented
    """
    #@synchronized(lock)
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            #cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    @synchronized(lock)
    def clear_instance(mcs):
        for instance in mcs._instances:
            del instance

        mcs._instances.clear()
