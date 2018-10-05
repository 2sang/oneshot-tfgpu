import sys

import docker
from absl import app, flags, logging

FLAGS = flags.FLAGS


def main(argv, client):
    print("This is run function")
    FLAGS(argv)
