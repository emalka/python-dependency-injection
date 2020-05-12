from py_common.decorators.autowired import autowired, AutoWiredType as Awt
from py_common.dependency_injection.test_dependency_injection.simple_injected_class import SimpleInjectedClass


class TestClassSinglecall:

    @autowired(Awt.SINGLECALL)
    def __init__(self, simple_injected_class: SimpleInjectedClass, my_name: str, no_type):
        self._simpleInjectedClass = simple_injected_class
        self.my_name = my_name

    def boo(self) -> str:
        return self._simpleInjectedClass.foo('hello')
