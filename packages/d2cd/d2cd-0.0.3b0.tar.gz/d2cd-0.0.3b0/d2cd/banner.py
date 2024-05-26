#!/usr/bin/env python3

"""Display Info"""

from .utils.docker_compose_utils import DockerComposeUtils
from .utils.git_utils import GitUtils
from .utils.logger import log


def display_info():
    ascii_banner = r"""
      _ ___         _
     | |__ \       | |
   __| |  ) |___ __| |
  / _` | / // __/ _` |
 | (_| |/ /| (_| (_| |
  \__,_|____\___\__,_|
    """
    log.info(f"Starting d2cd - Docker Compose Continuous Delivery {ascii_banner}")
    log.info(GitUtils.version())
    log.info(DockerComposeUtils.version())
