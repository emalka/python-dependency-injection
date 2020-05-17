from dependency_injection.decorators.autowired import autowired
from dependency_injection.decorators.autowired_enums import AutoWiredType
from dependency_injection.test_dependency_injection.Inject_abstract_muli_inherit import InjectedAbstractMuliInherit1, \
    InjectedAbstractMuliInherit2, InjectedDerivedAbstract2InjectedAbstractMuliInherit1, \
    InjectedDerivedAbstract2InjectedAbstractMuliInherit2


class TestAbstractClassMultiInherit:
    @autowired(
                AutoWiredType.SINGLETON,
                {
                    InjectedAbstractMuliInherit1: InjectedDerivedAbstract2InjectedAbstractMuliInherit1,
                    InjectedAbstractMuliInherit2: InjectedDerivedAbstract2InjectedAbstractMuliInherit2
                }
              )
    def __init__(self,
                 my_name: str,
                 no_name: str,
                 injected_abstract_multi_inherit1: InjectedAbstractMuliInherit1,
                 injected_abstract_multi_inherit2: InjectedAbstractMuliInherit2):
        self.injected_abstract_multi_inherit1 = injected_abstract_multi_inherit1
        self.injected_abstract_multi_inherit2 = injected_abstract_multi_inherit2
        self.my_name = my_name
        self.no_name = no_name

    def boo(self) -> str:
        return self.injected_abstract_multi_inherit1.foo('hello TestAbstractClassMultiInherit ')

    def goo(self) -> str:
        return self.injected_abstract_multi_inherit2.foo('hello TestAbstractClassMultiInherit ')

