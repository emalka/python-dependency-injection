from dependency_injection.decorators.autowired import autowired
from dependency_injection.test_dependency_injection.injected_class1 import InjectedClass
from dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2


class TestSingletonInjection:
    @autowired()
    def __init__(self, my_name: str, no_name: str, injected_class: InjectedClass, injected_class2: InjectedClass2):
        self.injected_class1 = injected_class
        self.my_name = my_name
        self.no_name = no_name
        self.injected_class2 = injected_class2

    def boo(self) -> str:
        return self.injected_class1.foo('hello TestClassSingleton')
