from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
import sys

import docker
import fire
from PyInquirer import prompt

from tfgpu.prompt_styles import custom_style_1, custom_style_2, custom_style_3
import tfgpu.utils as utils
import tfgpu.cli as cli


__version__ = '0.0.1'

PY3 = sys.version_info[0] >= 3


def check_initialized():
    conf = utils.load_conf()
    return conf['general']['initialized']


def _run(image_name='default'):
    if not check_initialized():
        return True
        # return _init()

    docker_client = docker.from_env()
    cli.run.run_container(image_name)
    return True


def _ls():
    pass


def _commit():
    pass


def _init():
    cli.init.create_new_image_prompt()


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
