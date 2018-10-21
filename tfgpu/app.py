from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
import sys

import docker
import fire

import tfgpu.utils as utils


def _run():
    print("this is run function")


def _ls():
    print("this is ls function")


def _commit():
    print("this is commit function")


def _init():
    print("this is init function")


def _ps():
    print("this is ps function")


def _set():
    print("this is set function")


def main():
    fire.Fire({
        'run': _run,
        'ls': _ls,
        'ps': _ps,
        'set': _set,
        'commit': _commit,
        'init': _init})


if __name__ == "__main__":
    main()
