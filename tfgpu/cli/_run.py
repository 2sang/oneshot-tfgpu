import sys

import docker
from absl import app, flags, logging

FLAGS = flags.FLAGS


def main(cli_args):
    print("This is run function")
    options = cli_args.options
    client = cli_args.client
    FLAGS(cli_args.args)

    return True
