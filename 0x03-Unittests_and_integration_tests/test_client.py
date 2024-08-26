#!/usr/bin/env python3
""" Clients test"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from client import GithubOrgClient
from functools import memoize


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient class test"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """test client.org"""
        client = GithubOrgClient(org)
        result = client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
        self.assertEqual(result, {"payload": True})

    @memoize
    @patch('client.get_json', return_value={"payload": True})
    def test_public_repos_url(self, mock_get_json):
        """test client._public_repos_url"""
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, {"payload": True})


if __name__ == "__main__":
    unittest.main()
