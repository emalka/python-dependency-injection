from unittest import TestCase

from py_common.data_structures.app_cache import AppCache
from py_common.dependency_injection.test_dependency_injection.test_class_singlecall import TestClassSinglecall
from py_common.dependency_injection.test_dependency_injection.test_class_singleton import TestClassSingleton


class TestInjection(TestCase):
    def test_constructor_injection(self) -> None:

        test_class_singleton: TestClassSingleton = TestClassSingleton()
        test_class_singleton.boo()

        test_class_singlecall: TestClassSinglecall = TestClassSinglecall()
        test_class_singlecall.boo()

