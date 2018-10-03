from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import sys
from os.path import dirname, basename, isfile

from absl import app, flags, logging

from tfgpu.cli import *
import tfgpu.exceptions as exep
import tfgpu.utils as utils


def main(argv):

    if len(argv) == 1:
        raise exep.CommandNotSpecified
        # Todo: logging.log Wed Oct  3 21:06:09 2018
    
    command = argv[1]
    modules = glob.glob(dirname(__file__) + "/cli/*.py")
    command_modules = {basename(f)[1:-3]: eval(basename(f)[:-3])
                       for f in modules
                       if isfile(f) and not f.endswith('__init__.py')}
    command_modules[command].execute()


if __name__ == "__main__":
    main(sys.argv)
