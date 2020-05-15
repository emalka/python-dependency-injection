from threading import Lock
from typing import Callable


class SingletonHandler:
    _lock: Lock = Lock()
    _class_locks: dict = {}
    _singletons: dict = {}

    @classmethod
    def add_singleton(cls, required_class: type, init_func: Callable, *args, **kwargs) -> object:
        # get specific class lock to avoid dead lock when creating singleton inside singleton
        cls._lock.acquire()
        if required_class.__name__ not in cls._class_locks:
            cls._class_locks[required_class.__name__] = Lock()
        class_lock = cls._class_locks.get(required_class.__name__, None)
        cls._lock.release()

        # using the class lock access the in
        class_lock.acquire()
        if required_class not in cls._singletons:
            cls._singletons[required_class] = init_func.__call__(*args, **kwargs)
        instance = cls._singletons[required_class]
        class_lock.release()

        return instance

    @classmethod
    def get_singleton(cls, required_class: type) -> object:
        # get specific class lock to avoid dead lock when creating singleton inside singleton
        cls._lock.acquire()
        if required_class.__name__ not in cls._class_locks:
            cls._class_locks[required_class.__name__] = Lock()
        class_lock = cls._class_locks.get(required_class.__name__, None)
        cls._lock.release()

        # using the class lock access the in
        instance: object = None
        class_lock.acquire()
        if required_class in cls._singletons:
            instance = cls._singletons[required_class]
        else:
            try:
                instance = required_class()
                cls._singletons[required_class] = instance
            except Exception as ex:
                instance = None
        class_lock.release()

        return instance

    @classmethod
    def remove_singleton(cls, required_class: type) -> object:
        # get specific class lock to avoid dead lock when creating singleton inside singleton
        cls._lock.acquire()
        if required_class.__name__ not in cls._class_locks:
            cls._class_locks[required_class.__name__] = Lock()
        class_lock = cls._class_locks.get(required_class.__name__, None)
        cls._lock.release()

        # using the class lock access the in
        class_lock.acquire()
        if required_class not in cls._singletons:
            return None
        instance = cls._singletons.pop(required_class)
        class_lock.release()

        return instance



