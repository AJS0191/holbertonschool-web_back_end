#!/usr/bin/env python3
"""the module contains unit testing"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
import utils


class TestAccessNestedMap(TestCase):
    """class that tests access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests that access nested map raises keyerrors"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)

    class TestGetJson(TestCase):
        """testing with mock http calls"""
        @parameterized.expand([
            "http://example.com", {"payload": True},
            "http://holberton.io", {"payload": False}
        ])
        @patch('utils.request.get')
        def test_get_json(self, tUrl, tPayload):
            """testing that get_json gets the correct payload"""
            self.assertEqual(get_json(tUrl), tPayload)


class TestMemoize(TestCase):
    """testing memoization"""
    def test_memoize():
        """memoize test"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a:
            memoTest = TestClass()
            memoTest.a_property
            memoTest.a_property
            mock_a.assert_called_once()
