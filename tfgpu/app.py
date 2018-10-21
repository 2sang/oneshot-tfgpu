from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
import sys

import docker
import fire
from PyInquirer import prompt

import tfgpu.cli
import tfgpu.utils as utils
from tfgpu.prompts import custom_style_1, custom_style_2, custom_style_3


__version__ = '0.0.1'

PY3 = sys.version_info[0] >= 3


def check_initialized():
    conf = utils.load_conf()
    return int(conf['general']['num_images']) != 0


def _run(image_name='default'):
    if not check_initialized():
        return _init()

    docker_client = docker.from_env()
    tfgpu.cli.run.run_container(image_name, docker_client)
    return True


def _ls():
    pass


def _commit():
    pass


def _init():
    tfgpu.cli.init.create_new_image_prompt()


def _ps():
    pass


def _set():
    pass


def main():
    if len(sys.argv) == 1:
        utils.print_usage()
        return False
    available_commands = ['run', 'ls', 'ps', 'set', 'init', 'commit']
    fire.Fire({command: eval('_' + command) for command in available_commands})


if __name__ == "__main__":
    main()
