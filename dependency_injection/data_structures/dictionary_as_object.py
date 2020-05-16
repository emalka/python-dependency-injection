import collections
import json
from typing import TypeVar


DictionaryAsObject = TypeVar('DictionaryAsObject', bound='DictionaryAsObject')
class DictionaryAsObject(collections.MutableMapping):

    # ToDo implement MutableMapping methods pop, popitem, clear, update, and setdefault they are inherited from parent

    def __init__(self, **kwargs):
        if kwargs:
            self.__dict__.update(**kwargs)

    def __getitem__(self, key):
        return getattr(self, str(key))

    def __setitem__(self, key, value):
        return setattr(self, str(key), value)

    def __contains__(self, key):
        return key in self.__dict__

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, attr):
        attr = str(attr)

        value = self.__dict__.get(str(attr), None)

        if value:
            return value

        return None

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, v) -> None:
        self.__dict__.__delitem__(v)

    def __iter__(self):
        return self.__dict__.__iter__()

    def __eq__(self, other):
        if isinstance(other, DictionaryAsObject):
            return self.__dict__ == other.__dict__
        elif isinstance(other, dict):
            return self.__dict__ == other

        return False

    def get(self, k, d=None):
        return self.__dict__.get(k, d)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_json(cls, json_data: str) -> DictionaryAsObject:
        return cls.from_dict(json.loads(json_data))

    @classmethod
    def from_dict(cls, dict_data: dict) -> DictionaryAsObject:
        obj_dict: DictionaryAsObject = DictionaryAsObject()

        for key, value in dict_data.items():
            if type(value) == dict:
                obj_dict[key] = cls.from_dict(value)
            else:
                obj_dict[key] = value

        return obj_dict
