#!/usr/bin/env python3

"""
Git Utils
"""

import asyncio
import os

from git import Git, InvalidGitRepositoryError, NoSuchPathError, Repo
from giturlparse import parse

from .errors import NoGitAuthenticationError
from .logger import log


class GitUtils:
    BASE_LOCATION = "/opt/d2cd"

    def __init__(self, branch, repo_url, auth=None):
        self.repo_url = repo_url
        self.auth = auth
        self.branch = branch
        self.parsed_git_url = parse(self.repo_url)
        self.repo_location = os.path.join(
            GitUtils.BASE_LOCATION,
            self.parsed_git_url.host,
            self.parsed_git_url.owner,
            self.parsed_git_url.name,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @staticmethod
    def version():
        return Git().version().capitalize()

    def _is_git_repo(self, repo_location):
        try:
            git_repo = Repo(repo_location)
            return git_repo
        except (InvalidGitRepositoryError, NoSuchPathError):
            return None

    def clone_repository(self):
        git_ssh_cmd = ""

        if self._is_git_repo(self.repo_location) is not None:
            log.info(f"Repo already exists in {self.repo_location}")
            return None

        if self.auth.get("ssh_key_location"):
            log.info("Authentication using ssh key for git")
            git_ssh_cmd = f"ssh -i {self.auth['ssh_key_location']}"
        elif self.auth.get("username") and self.auth.get("password"):
            log.info("Authentication using username and password for git")
            username = self.auth["username"]
            password = self.auth["password"]
            self.repo_url = f"https://{username}:{password}@{self.parsed_git_url.host}/{self.parsed_git_url.owner}/{self.parsed_git_url.name}.git"
        else:
            raise NoGitAuthenticationError("Authentication details not provided")

        git_ssh_cmd += f" -o StrictHostKeyChecking=no"

        log.info(
            f"Clone git repository {self.parsed_git_url.name} in {self.repo_location}"
        )
        with Repo.clone_from(
            url=self.repo_url,
            to_path=self.repo_location,
            env={"GIT_SSH_COMMAND": git_ssh_cmd},
        ) as repo:
            repo.git.checkout(self.branch)

        return None

    def pull_changes(self):
        log.info(f"Run git pull in {self.repo_location}")
        with Repo(self.repo_location) as repo:
            old_commit_id = repo.head.commit.hexsha
            origin = repo.remotes.origin
            origin.fetch()
            repo.git.checkout(self.branch)
            origin.pull()
            return old_commit_id != repo.head.commit.hexsha

    # ========================== asyncio wrapper methods ==========================

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass

    async def pull_changes_async(self):
        result = await asyncio.to_thread(self.pull_changes)
        return result
