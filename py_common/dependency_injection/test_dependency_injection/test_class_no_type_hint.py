from py_common.decorators.autowired import autowired
from py_common.dependency_injection.test_dependency_injection.injected_class1 import InjectedClass1
from py_common.dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2


class TestClassNoTypeHint:

    @autowired()
    def __init__(self, my_name: str, no_name: str, injected_class1: InjectedClass1, injected_class2):
        self.injected_class1 = injected_class1
        self.my_name = my_name
        self.no_name = no_name
        self.injected_class2 = injected_class2

    def boo(self) -> str:
        return self.injected_class1.foo('hello TestClassNoTypeHint')