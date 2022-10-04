#!/usr/bin/env python3
"""the module contains unit testing"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
import pytest


class TestAccessNestedMap(TestCase):
    """class that tests access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests that access nested map raises keyerrors"""
        self.assertRaises(KeyError, access_nested_map(nested_map, path))
