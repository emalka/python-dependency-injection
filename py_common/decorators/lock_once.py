import inspect
from threading import Lock
from typing import Callable


class LockOnce:
    def __init__(self, func: Callable):

        eli = inspect.getmembers(func)

        self.func: Callable = func
        self.mutex: Lock = Lock()

    def __call__(self, *args, **kwargs):
        with self.mutex:
            self.func(self.func.__call__, *args, **kwargs)
