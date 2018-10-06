import sys
import logging

import docker
from absl import app, flags, logging

import tfgpu.exceptions as exep

FLAGS = flags.FLAGS

flags.DEFINE_string("hello", None, "Your name")

def main(cli_args):
    print("This is run function")
    options = cli_args.options
    client = cli_args.client
    print("options: {}".format(options))
    FLAGS(cli_args.args)

    if not options:
        logging.warning("Specify image(tfgpu run [IMAGE_NAME])")
        logging.warning("To see available images: tfgpu image ls")
        raise exep.CommandNotSpecified

    return True
