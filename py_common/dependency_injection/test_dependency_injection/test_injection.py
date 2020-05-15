from unittest import TestCase

from py_common.dependency_injection.dependency_injection_exception import DependencyInjectionException
from py_common.dependency_injection.test_dependency_injection.injected_class1 import InjectedClass1
from py_common.dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2
from py_common.dependency_injection.test_dependency_injection.test_class_no_type_hint import TestClassNoTypeHint
from py_common.dependency_injection.test_dependency_injection.test_class_singlecall import TestClassSinglecall
from py_common.dependency_injection.test_dependency_injection.test_class_singleton import TestClassSingleton


class TestInjection(TestCase):
    def test_no_injection(self) -> None:
        try:
            test_class_singleton: TestClassSingleton = TestClassSingleton('my_name', 'no_name', InjectedClass1(), InjectedClass2())
        except Exception as ex:
            pass
        ret_val: str = test_class_singleton.boo()
        self.assertEqual('hello TestClassSingleton from InjectedClass1', ret_val)

        try:
            test_class_singleton: TestClassSingleton = TestClassSingleton('my_name', 'no_name')
        except Exception as ex:
            pass
        ret_val: str = test_class_singleton.boo()
        self.assertEqual('hello TestClassSingleton from InjectedClass1', ret_val)

    def test_injection_with_builtin_types_exception(self) -> None:
        try:
            # No injection all parameters are passed. all ok.
            test_class_no_hint_type: TestClassNoTypeHint = TestClassNoTypeHint('my_name', 'no_name', InjectedClass1(), InjectedClass2())
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

    def test_no_injection_singlecall(self) -> None:
        try:
            test_class_singlecall: TestClassSinglecall = TestClassSinglecall('my_name', 'no_name', InjectedClass1(), InjectedClass2())
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


