#!/usr/bin/env python3

"""Unittest class for utils.py"""

from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """
    the test access nested map
    test cases class.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Assert the output is equal to the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_key_error(self, nested_map, path):
        """
        Assert the output is equal to the expected result.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
