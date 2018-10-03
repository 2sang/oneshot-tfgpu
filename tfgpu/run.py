from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import sys
from os.path import dirname, basename, isfile

from tfgpu.cli import *
import tfgpu.exceptions as exep
import tfgpu.utils as utils


class Command:
    modules = glob.glob(dirname(__file__) + "/cli/*.py")
    command_modules = {basename(f)[1:-3]: eval(basename(f)[:-3])
                       for f in modules
                       if isfile(f) and not f.endswith('__init__.py')}

    def __init__(self, argv):
        if len(argv) == 1:
            raise exep.CommandNotSpecified
            # Todo: logging.log Wed Oct  3 21:06:09 2018

        self.command, self.options = argv[1], argv[2:]

        if self.command not in self.command_modules.keys():
            raise exep.WrongCommandName

        self.module = self.command_modules[self.command]
        self.module_filename = '_' + self.command + '.py'
        print("self.module_filename: {}".format(self.module_filename))
        print("self.options: {}".format(self.options))

    def execute(self):
        self.module.main(list(self.module_filename) + list(self.options))


def main(argv):
    command = Command(argv)
    command.execute()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise exep.CommandNotSpecified
    main(sys.argv)
