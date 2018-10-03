from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from absl import app, flags, logging

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
    print("argv: {}".format(argv))


if __name__ == "__main__":
    main()
