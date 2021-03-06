from dependency_injection.decorators.autowired import autowired
from dependency_injection.decorators.autowired_enums import AutoWiredType
from dependency_injection.test_dependency_injection.injected_class1 import InjectedClass
from dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2


class TestClassSinglecall:

    @autowired(AutoWiredType.SINGLECALL)
    def __init__(self, my_name: str, no_name: str, injected_class1: InjectedClass, injected_class2: InjectedClass2):
        self.injected_class1 = injected_class1
        self.my_name = my_name

    def boo(self) -> str:
        return self.injected_class1.foo('hello TestClassSinglecall')
