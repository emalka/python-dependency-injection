from unittest import TestCase

from py_common.data_structures.app_cache import AppCache


class TestAppCache(TestCase):
    def test_put_app_cache(self) -> None:
        app_cache = AppCache()
        app_cache.put('eli', 'hagadol')
        p1 = app_cache.get('eli')
        self.assertEqual(p1, 'hagadol')
