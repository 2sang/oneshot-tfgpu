from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
from os.path import dirname, basename, isfile
import sys

import docker

from tfgpu.cli import *
import tfgpu.exceptions as exep
import tfgpu.utils as utils


class Command:

    def __init__(self, argv=None):
        pass


def main():
    if len(sys.argv) == 1:
        raise exep.CommandNotSpecified
    command = Command(sys.argv[1:])
    command.execute()


if __name__ == "__main__":
    main()
