from unittest import TestCase

from py_common.data_structures.app_cache import AppCache
from py_common.dependency_injection.test_dependency_injection.test_class import TestClass


class TestInjection(TestCase):
    def test_constructor_injection(self) -> None:

        test_class: TestClass = TestClass()
        test_class.boo()
