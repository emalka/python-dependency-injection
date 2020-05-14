from unittest import TestCase

from py_common.data_structures.app_cache import AppCache
from py_common.dependency_injection.test_dependency_injection.injected_class1 import InjectedClass1
from py_common.dependency_injection.test_dependency_injection.injected_class2 import InjectedClass2
from py_common.dependency_injection.test_dependency_injection.test_class_singlecall import TestClassSinglecall
from py_common.dependency_injection.test_dependency_injection.test_class_singleton import TestClassSingleton


class TestInjection(TestCase):
    def test_constructor_injection(self) -> None:

        test_class_singleton: TestClassSingleton = TestClassSingleton('my_name', InjectedClass1(), 'no_name', InjectedClass2())
        test_class_singleton.boo()

        test_class_singleton: TestClassSingleton = TestClassSingleton(my_name='first_param')
        test_class_singleton.boo()

        test_class_singleton: TestClassSingleton = TestClassSingleton('my_name', InjectedClass1(), injected_class2=InjectedClass2(), no_name='no_name')
        test_class_singleton.boo()


        test_class_singlecall: TestClassSinglecall = TestClassSinglecall()
        test_class_singlecall.boo()

