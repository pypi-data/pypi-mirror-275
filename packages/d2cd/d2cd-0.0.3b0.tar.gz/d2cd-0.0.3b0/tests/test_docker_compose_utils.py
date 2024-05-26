#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock, patch

from d2cd.utils.docker_compose_utils import DockerComposeUtils


class TestDockerComposeUtils(unittest.TestCase):
    @patch("docker_compose_utils.DockerClient")
    def test_version(self, mock_docker_client):
        # Mocking the docker-compose version method to return a specific value
        mock_docker_client.return_value.compose.version.return_value = "1.2.3"
        self.assertEqual(DockerComposeUtils.version(), "1.2.3")

    @patch("docker_compose_utils.DockerClient")
    def test_up(self, mock_docker_client):
        # Mocking the docker-compose up method
        mock_instance = mock_docker_client.return_value.__enter__.return_value
        docker_utils = DockerComposeUtils(compose_files=["docker-compose.yml"])
        docker_utils.up()
        mock_instance.compose.up.assert_called_once_with(
            detach=True, quiet=True, build=True, remove_orphans=True, pull="always"
        )

    @patch("docker_compose_utils.DockerClient")
    def test_ps(self, mock_docker_client):
        # Mocking the docker-compose ps method
        mock_instance = mock_docker_client.return_value.__enter__.return_value
        docker_utils = DockerComposeUtils(compose_files=["docker-compose.yml"])
        docker_utils.ps()
        mock_instance.compose.ps.assert_called_once()

    @patch("docker_compose_utils.DockerClient")
    def test_restart(self, mock_docker_client):
        # Mocking the docker-compose restart method
        mock_instance = mock_docker_client.return_value.__enter__.return_value
        docker_utils = DockerComposeUtils(compose_files=["docker-compose.yml"])
        docker_utils.restart()
        mock_instance.compose.restart.assert_called_once()

    @patch("docker_compose_utils.DockerClient")
    def test_ls(self, mock_docker_client):
        # Mocking the docker-compose ls method
        mock_instance = mock_docker_client.return_value.__enter__.return_value
        docker_utils = DockerComposeUtils(compose_files=["docker-compose.yml"])
        docker_utils.ls()
        mock_instance.compose.ls.assert_called_once()

    @patch("docker_compose_utils.DockerClient")
    def test_down(self, mock_docker_client):
        # Mocking the docker-compose down method
        mock_instance = mock_docker_client.return_value.__enter__.return_value
        docker_utils = DockerComposeUtils(compose_files=["docker-compose.yml"])
        docker_utils.down()
        mock_instance.compose.down.assert_called_once()


if __name__ == "__main__":
    unittest.main()
