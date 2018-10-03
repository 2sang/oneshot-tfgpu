from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from absl import app, flags, logging

import utils

MODULE_EXTENSIONS = ['.py']
FLAGS = flags.FLAGS
defaults = {
    'tag': 'latest-gpu-py3',
    'volume_name': 'tfgpu-volume'
}

flags.DEFINE_string('tag', defaults['tag'],
                    'image tag name(ex. latest-gpu-py3)')
flags.DEFINE_string('vname', defaults['volume_name'],
                    'specify the volume name to mount')


class TfgpuImage:
    """Tfgpu image class def"""
    def __init__(self):
        pass


def main(argv):
    available_commands = ['init', 'run', 'commit', 'set', 'ps', 'ls']
    command = argv[1]
    if command not in available_commands:
        print("not available command: {}".format(command))
        return;


if __name__ == "__main__":
    main(sys.argv)
