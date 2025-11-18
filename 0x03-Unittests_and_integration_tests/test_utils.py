#!/usr/bin/env python3
'''
Unittest for access_nested_map function
'''
import unittest
from unittest.mock import patch, Mock, MagicMock
from typing import Dict, Sequence, Mapping, Any, Dict
from parameterized import parameterized # type: ignore
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize =  __import__('utils').memoize
import requests
from requests.models import Request


class TestAccessNestedMap(unittest.TestCase):
    ''' define testcases for the function access_nested_map
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        ''' make sure the method returns required result '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        ''' make sure KeyError is raised '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' Test the get_json function
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: MagicMock) -> None:
        # configure the mock objects return value
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    ''' test the memoize function '''
    def test_memoize(self) -> None:
        ''' test the func '''
        class TestClass:

            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()
        

        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()


if __name__ == '__main__':
    unittest.main()
