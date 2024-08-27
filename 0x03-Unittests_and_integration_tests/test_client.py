#!/usr/bin/env python3
""" Clients test"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from utils import memoize


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test client.public_repos"""
        fake_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}}
        ]
        mock_get_json.return_value = fake_repos_payload
        with patch.object(
             GithubOrgClient,
             '_public_repos_url',
             new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://mock_url"
            client = GithubOrgClient("testorg")
            result = client.public_repos()
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://mock_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test the has_license method of GithubOrgClient."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
