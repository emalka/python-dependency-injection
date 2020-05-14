from threading import Lock

from py_common.data_structures.app_cache import AppCache
from py_common.design_patterns.singleton import Singleton


class Context(metaclass=Singleton):
    def __init__(self):
        self._cache = AppCache()


context: Context = Context()
