from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

import tfgpu.utils as utils

# These need test too
HOST_PYTHON = 'python3'
RUNFILE = 'app.py'
DOTFILE = '~/.tfgpu'
# Todo: Consider OS dependent rc file Tue Oct  2 09:05:25 2018
BASHRC = '~/.bashrc'

INSTALLFILE_PATH = os.path.realpath(__file__)
RUNFILE_PATH = os.path.join(os.path.dirname(INSTALLFILE_PATH), RUNFILE)
TFGPU_DOTFILE_PATH = os.path.expanduser(DOTFILE)  # Default: ~/.tfgpu
TFGPU_SOURCE_STRING = 'source  ' + TFGPU_DOTFILE_PATH + '\n'
BASHRC_PATH = os.path.expanduser(BASHRC)


def check_prerequisites():
    # TODO: tfgpu dependencies(pip2, pip3)
    if False:
        raise PrerequisiteNotSatisfied
    # check nvidia driver dependencies
    return True


def build_shell_commands():
    with open(TFGPU_DOTFILE_PATH, 'w') as tfgpu:
        tfgpu.write('alias tfgpu="' + HOST_PYTHON + ' ' + RUNFILE_PATH + '"\n')
    with open(BASHRC_PATH, 'a') as bashrc:
        bashrc.write(TFGPU_SOURCE_STRING)


def teardown_shell_commands():
    utils.remove_line_from_file(BASHRC_PATH, TFGPU_SOURCE_STRING)
    if os.path.exists(TFGPU_DOTFILE_PATH):
        os.remove(TFGPU_DOTFILE_PATH)


def install():
    if os.path.exists(os.path.expanduser('~/.tfgpu')):
        print("tfgpu exists. exit")
        return False
    build_shell_commands()
    return True


def main(argv):
    if 'uninstall' in argv:
        teardown_shell_commands()
        return
    # Todo: Sanity check for --runtime=nvidia option Mon 01 Oct 2018
    if not (check_prerequisites()):
        print("prerequisites not satistied")
        return
    install()


class PrerequisiteNotSatisfied(Exception):
    pass


if __name__ == "__main__":
    main(sys.argv)
