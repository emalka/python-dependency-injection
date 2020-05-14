from py_common.decorators.autowired import autowired
from py_common.decorators.autowired_enums import AutoWiredType as Awt
from py_common.dependency_injection.test_dependency_injection.injected_class1 import InjectedClass1


class TestClassSinglecall:

    @autowired(Awt.SINGLECALL)
    def __init__(self, simple_injected_class: InjectedClass1, my_name: str, no_type):
        self._simpleInjectedClass = simple_injected_class
        self.my_name = my_name

    def boo(self) -> str:
        return self._simpleInjectedClass.foo('hello')
