from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
from os.path import dirname, basename, isfile
import sys

import docker
import fire

from tfgpu.cli import *
import tfgpu.exceptions as exep
import tfgpu.utils as utils


class Command:

    def __init__(self, argv=None):
        pass


def execute(commands):
    if not commands:
        print("will run default command")
    modules_dict = utils.load_modules_dict()
    return eval(modules_dict[commands]).main()


def main():
    fire.Fire(execute)


if __name__ == "__main__":
    main()
