from unittest import TestCase

from dependency_injection.data_structures.dependency_injection_exception import DependencyInjectionException
from dependency_injection.test_dependency_injection.injected_class1 import InjectedClass
from dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2
from dependency_injection.test_dependency_injection.test_class_no_type_hint import TestClassNoTypeHint
from dependency_injection.test_dependency_injection.test_class_singlecall import TestClassSinglecall
from dependency_injection.test_dependency_injection.test_class_singleton import TestSingletonInjection


class TestInjection(TestCase):
    def test_injection_singleton(self) -> None:
        try:
            test_class_singleton: TestSingletonInjection = TestSingletonInjection('my_name', 'no_name', InjectedClass(), InjectedClass2())
        except Exception as ex:
            pass
        ret_val: str = test_class_singleton.boo()
        self.assertEqual('hello TestClassSingleton from InjectedClass1', ret_val)

        try:
            test_class_singleton: TestSingletonInjection = TestSingletonInjection('my_name', 'no_name')
        except Exception as ex:
            pass
        ret_val: str = test_class_singleton.boo()
        self.assertEqual('hello TestClassSingleton from InjectedClass1', ret_val)

    def test_injection_with_builtin_types_exception(self) -> None:
        try:
            # No injection all parameters are passed. all ok.
            test_class_no_hint_type: TestClassNoTypeHint = TestClassNoTypeHint('my_name', 'no_name', InjectedClass(), InjectedClass2())
        except DependencyInjectionException as ex:
            pass

        ret_val: str = test_class_no_hint_type.boo()
        self.assertEqual('hello TestClassNoTypeHint from InjectedClass1', ret_val)

        try:
            # No type hint for class InjectedClass2 in TestClassNoTypeHint __init__
            test_class_no_hint_type: TestClassNoTypeHint = TestClassNoTypeHint('my_name', 'no_name',)
        except DependencyInjectionException as ex:
            self.assertEqual(ex.exception_description, 'type hints must be used in order to inject a type. param_name=[injected_class2]')

    def test_injection_no_type_hint(self):
        try:
            test_class_no_type_hint: TestClassNoTypeHint = TestClassNoTypeHint('my_name')
        except DependencyInjectionException as ex:
            self.assertEqual(ex.exception_description, 'Cannot inject builtin types. param_type=[str] param_name=[no_name]')

    def test_injection_singlecall(self) -> None:
        try:
            test_class_singlecall: TestClassSinglecall = TestClassSinglecall('my_name', 'no_name', InjectedClass(), InjectedClass2())
        except Exception as ex:
            pass
        ret_val: str = test_class_singlecall.boo()
        self.assertEqual('hello TestClassSinglecall from InjectedClass1', ret_val)

        try:
            test_class_singlecall: TestClassSinglecall = TestClassSinglecall('my_name', 'no_name')
        except Exception as ex:
            pass
        ret_val: str = test_class_singlecall.boo()
        self.assertEqual('hello TestClassSinglecall from InjectedClass1', ret_val)


