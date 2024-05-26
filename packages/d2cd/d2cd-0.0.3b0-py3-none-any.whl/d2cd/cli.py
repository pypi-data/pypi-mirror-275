#!/usr/bin/env python3

"""
CLI Arguments
"""

import argparse
import os

from . import __version__


class EnvDefault(argparse.Action):
    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def parse_arguments():
    """Argument parser"""
    parser = argparse.ArgumentParser(
        description="d2cd - Docker Compose Continuous Delivery",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-c",
        "--config-file",
        action=EnvDefault,
        envvar="CONFIG_FILE",
        type=str,
        required=True,
        help="Config file location",
    )

    parser.add_argument(
        "-s",
        "--sleep-time",
        type=int,
        default=600,
        help="Sleep time for each reconciliation",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Enale debug mode",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s v{__version__}",
        help="Show d2cd version",
    )

    return parser.parse_args()
