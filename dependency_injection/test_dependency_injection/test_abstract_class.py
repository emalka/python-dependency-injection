from dependency_injection.decorators.autowired import autowired
from dependency_injection.test_dependency_injection.injected_abstract import InjectedAbstract


class TestAbstractClass:
    @autowired()
    def __init__(self, my_name: str, no_name: str, injected_abstract: InjectedAbstract):
        self.injected_abstract = injected_abstract
        self.my_name = my_name
        self.no_name = no_name

    def boo(self) -> str:
        return self.injected_abstract.foo('hello TestAbstractClass ')
