#!/usr/bin/env python3

"""
Main module
"""

import asyncio
import os
import sys

from .banner import display_info
from .cli import parse_arguments
from .config_loader import ConfigLoader
from .utils.docker_compose_utils import DockerComposeUtils
from .utils.git_utils import GitUtils
from .utils.logger import log


async def reconcile_repos(repo):
    async with GitUtils(branch=repo["branch"], repo_url=repo["url"]) as gt:
        if await gt.pull_changes_async():
            for compose_path in repo["docker_compose_paths"]:
                full_path = os.path.join(gt.repo_location, compose_path)
                async with DockerComposeUtils(compose_files=[full_path]) as dc:
                    await dc.up_async()
        else:
            log.info("No changes in upstream git repo")


async def reconcilation_loop(config):
    log.info("Starting reconcilation in loop..")
    while True:
        await asyncio.sleep(config["sync_interval_seconds"])
        tasks = []
        for repo in config["repos"]:
            tasks.append(reconcile_repos(repo))
        await asyncio.gather(*tasks)


def initialize_repos(config):
    for repo in config["repos"]:
        with GitUtils(
            branch=repo["branch"], repo_url=repo["url"], auth=repo["auth"]
        ) as gt:
            gt.clone_repository()
            for compose_path in repo["docker_compose_paths"]:
                full_path = os.path.join(gt.repo_location, compose_path)
                with DockerComposeUtils(compose_files=[full_path]) as dc:
                    dc.up()


def main():
    args = parse_arguments()

    log.remove()
    log.add(sys.stderr, level="DEBUG" if args.debug else "INFO")

    cfg = ConfigLoader(config_file=args.config_file)
    config = cfg.get_config()

    display_info()

    initialize_repos(config)
    asyncio.run(reconcilation_loop(config))
