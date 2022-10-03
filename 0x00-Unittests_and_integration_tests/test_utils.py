#!/usr/bin/env python3
"""the module contains unit testing"""
from unittest import TestCase, assertEq
import parameterized
from utils import access_nested_map
import pytest


class TestAccessNestedMap(TestCase):
    """class that tests access nested map"""
    def __init__(self) -> None:
        super().__init__()

    @parameterized.expand
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access nested map"""
        self.assertEq(access_nested_map(nested_map, path), expected)
