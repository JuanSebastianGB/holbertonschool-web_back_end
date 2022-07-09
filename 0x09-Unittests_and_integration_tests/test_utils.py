#!/usr/bin/env python3

"""Unittest class for utils.py"""

from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch


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
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Assert the output is equal to the expected result.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """
        Assert the output is equal to the expected result.
        """
        with patch('requests.get') as executed_function:
            executed_function.return_value.json.return_value = expected
            response = get_json(url)
            self.assertEqual(response, expected)
            executed_function.assert_called_once()
