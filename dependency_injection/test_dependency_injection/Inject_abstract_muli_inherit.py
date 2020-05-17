from abc import ABC, abstractmethod


class InjectedAbstractMuliInherit1(ABC):
    def __init__(self):
        super().__init__()
        self.message = 'InjectedAbstractMuliInherit1'

    @abstractmethod
    def foo(self, str1: str) -> str:
        pass


class InjectedDerivedAbstract1InjectedAbstractMuliInherit1(InjectedAbstractMuliInherit1):

    def __init__(self):
        super().__init__()
        self.message += ' + InjectedDerivedAbstract1InjectedAbstractMuliInherit1'

    def foo(self, str1: str) -> str:
        return str1 + self.message


class InjectedDerivedAbstract2InjectedAbstractMuliInherit1(InjectedAbstractMuliInherit1):

    def __init__(self):
        super().__init__()
        self.message += ' + InjectedDerivedAbstract2InjectedAbstractMuliInherit1'

    def foo(self, str1: str) -> str:
        return str1 + self.message


class InjectedAbstractMuliInherit2(ABC):
    def __init__(self):
        super().__init__()
        self.message = 'InjectedAbstractMuliInherit2'

    @abstractmethod
    def foo(self, str1: str) -> str:
        pass


class InjectedDerivedAbstract1InjectedAbstractMuliInherit2(InjectedAbstractMuliInherit2):

    def __init__(self):
        super().__init__()
        self.message += ' + InjectedDerivedAbstract1InjectedAbstractMuliInherit2'

    def foo(self, str1: str) -> str:
        return str1 + self.message


class InjectedDerivedAbstract2InjectedAbstractMuliInherit2(InjectedAbstractMuliInherit2):

    def __init__(self):
        super().__init__()
        self.message += ' + InjectedDerivedAbstract2InjectedAbstractMuliInherit2'

    def foo(self, str1: str) -> str:
        return str1 + self.message
