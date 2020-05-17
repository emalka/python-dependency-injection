from abc import ABC, abstractmethod


class InjectedAbstract(ABC):
    def __init__(self):
        super().__init__()
        self.message = 'InjectedAbstract'

    @abstractmethod
    def foo(self, str1: str) -> str:
        pass


class InjectedDerivedAbstract(InjectedAbstract):

    def __init__(self):
        super().__init__()
        self.message += ' + InjectedDerivedAbstract'

    def foo(self, str1: str) -> str:
        return str1 + self.message

