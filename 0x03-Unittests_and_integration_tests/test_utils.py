#!/usr/bin/env python3
""" Utils test"""

from parameterized import parameterized #type: ignore
import unittest
from unittest.mock import patch
from typing import Any, Dict, Tuple, Type

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
         ({"a": 1}, ("a",), 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any], path: Tuple[str], expected: Any) -> None:
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map: Dict[Any, Any], path: Tuple[str], exception: Type[BaseException]) -> None:
        """testint nested maps"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tests https requests"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload", False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool], test_get: Any) -> None:
        """test get_json function"""
        test_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """does memoization tests"""
    def test_memoize(self) -> None:
        """test memoize"""
        class TestClass:
            """test class"""
            def a_method(self) -> int:
                """a method"""
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            tc = TestClass()
            # calling twice to ensure it was called only once
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
