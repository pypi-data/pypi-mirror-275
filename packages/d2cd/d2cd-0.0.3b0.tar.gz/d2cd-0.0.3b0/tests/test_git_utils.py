#!/usr/bin/env python3


import unittest
from unittest.mock import patch

from d2cd.utils.git_utils import GitUtils


class TestGitUtils(unittest.TestCase):
    def test_version(self):
        # Mocking the Git version method to return a specific value
        with patch("git_utils.Git") as mock_git:
            mock_git.return_value.version.return_value = "1.2.3"
            self.assertEqual(GitUtils.version(), "1.2.3")

    def test_is_git_repo_exists(self):
        # Test case when the Git repository exists
        git_utils = GitUtils(branch="main", repo_url="https://github.com/user/repo.git")
        self.assertTrue(git_utils._is_git_repo("/path/to/existing/repo"))

        # Test case when the Git repository does not exist
        self.assertFalse(git_utils._is_git_repo("/path/to/nonexistent/repo"))

    def test_pull_changes(self):
        # Mocking the Git pull method to simulate changes being pulled
        with patch("git_utils.Repo") as mock_repo:
            mock_instance = mock_repo.return_value.__enter__.return_value
            mock_instance.head.commit.hexsha = "old_commit_id"
            mock_instance.remotes.origin.pull.return_value = True
            git_utils = GitUtils(
                branch="main", repo_url="https://github.com/user/repo.git"
            )
            self.assertTrue(git_utils.pull_changes())

        # Mocking the Git pull method to simulate no changes being pulled
        with patch("git_utils.Repo") as mock_repo:
            mock_instance = mock_repo.return_value.__enter__.return_value
            mock_instance.head.commit.hexsha = "same_commit_id"
            mock_instance.remotes.origin.pull.return_value = True
            git_utils = GitUtils(
                branch="main", repo_url="https://github.com/user/repo.git"
            )
            self.assertFalse(git_utils.pull_changes())


if __name__ == "__main__":
    unittest.main()
