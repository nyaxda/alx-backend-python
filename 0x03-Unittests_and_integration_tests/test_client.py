#!/usr/bin/env python3
""" Clients test"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """test client.org"""
        mock_get_json.return_value = {"payload": True}
        client = GithubOrgClient(org)
        result = client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == "__main__":
    unittest.main()
