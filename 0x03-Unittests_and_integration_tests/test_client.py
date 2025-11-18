#!/usr/bin/env python3
''' Test classes and methods in client.py
'''
GithubOrgClient = __import__('client').GithubOrgClient
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized # type: ignore
from parameterized import parameterized_class
from typing import Mapping
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the class GithubOrgClient
    """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, input_str: str, mock_method: MagicMock) -> None:
        """ test the return value of GithubOrgClient.org
        """
        test_obj = GithubOrgClient(input_str)
        test_obj.org()
        mock_method.called_with_once(test_obj.ORG_URL.format(org=input_str))

    def test_public_repos_url(self) -> None:
        """ test GithubOrgClient._public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json: MagicMock) -> None:
        """ test GithubOrgClient._public_repos
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            payload = [{"name": "Google"}, {"name": "Twitter"}]
            mock_json.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)

            mock.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Mapping, license_key: str, expected: bool) -> None:
        """ unit-test GithubOrgClient.has_license
        """
        # it's a staticmethod so can be done this way
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for GithubOrgClient.public_repos
        Only mock code that sends external requests
    """
    @classmethod
    def setUpClass(cls):
        """ set up before each test """
        config = {"return_value.json.side_effect":
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                 }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ method that tears down test objects and params
        """
        cls.get_patcher.stop()
