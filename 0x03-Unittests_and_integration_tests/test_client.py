#!/usr/bin/env python3
""" Clients test"""

from parameterized import parameterized
from parameterized import parameterized_class
import unittest
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
from utils import memoize
import fixtures


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


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the class by mocking requests.get"""
        cls.get_patcher = patch(
             'requests.get',
             side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mock requests.get behavior"""
        if url == GithubOrgClient.ORG_URL.format(org='testorg'):
            return Mock(json=lambda: fixtures.org_payload)
        if url == fixtures.org_payload['repos_url']:
            return Mock(json=lambda: fixtures.repos_payload)
        return None

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient("testorg")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with a license filter"""
        client = GithubOrgClient("testorg")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
