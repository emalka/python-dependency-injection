from py_common.decorators.autowired import autowired
from py_common.decorators.autowired_enums import AutoWiredType as Awt
from py_common.dependency_injection.test_dependency_injection.injected_class1 import InjectedClass1
from py_common.dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2


class TestClassSinglecall:

    @autowired(Awt.SINGLECALL)
    def __init__(self, my_name: str, no_name: str, injected_class1: InjectedClass1, injected_class2: InjectedClass2):
        self.injected_class1 = injected_class1
        self.my_name = my_name

    def boo(self) -> str:
        return self.injected_class1.foo('hello TestClassSinglecall')
