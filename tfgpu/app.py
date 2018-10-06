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


class CliArguments:
    def __init__(self, args, client):
        self.args = args
        self.module_filename = self.args[0]
        self.options = self.args[1:]
        self.client = client


class Command:
    modules = glob.glob(dirname(__file__) + "/cli/*.py")
    command_modules = {basename(f)[1:-3]: eval(basename(f)[:-3])
                       for f in modules
                       if isfile(f) and not f.endswith('__init__.py')}

    def __init__(self, argv=None):
        if not argv:
            raise exep.CommandNotSpecified()

        self.command, self.options = argv[0], argv[1:]

        if self.command not in self.command_modules.keys():
            logging.error("No such command: {}".format(self.command))
            raise exep.NoSuchCommand(self.command)

        self.module = self.command_modules[self.command]
        self.module_filename = '_' + self.command + '.py'

    def execute(self):
        client = docker.from_env()
        cli_component = CliArguments([self.module_filename,
                                     *self.options],
                                     client)
        return self.module.main(cli_component)

    def clear_options(self):
        self.options = None

    def append_option(self, options):
        if type(options) == list:
            self.options += options
        elif type(options) == str:
            self.options.append(options)
        else:
            raise TypeError


def main():
    if len(sys.argv) == 1:
        raise exep.CommandNotSpecified
    command = Command(sys.argv[1:])
    command.execute()


if __name__ == "__main__":
    main()
