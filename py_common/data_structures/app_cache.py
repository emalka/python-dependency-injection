from threading import Lock

from py_common.data_structures.dictionary_as_object import DictionaryAsObject
from py_common.decorators.lock_once import LockOnce
from py_common.decorators.synchronized import synchronized
from py_common.design_patterns.singleton import Singleton


class AppCache(metaclass=Singleton):
    def __init__(self):
        # will be used by @synchronized()
        self.lock: Lock = Lock()
        self._cache: DictionaryAsObject = DictionaryAsObject()

    @synchronized()
    def put(self, key: any, value: any) -> None:
        self._cache[key] = value

    @synchronized()
    def get(self, key) -> any:
        ret_val: any = None
        if key in self._cache:
            ret_val = self._cache[key]
        return ret_val
