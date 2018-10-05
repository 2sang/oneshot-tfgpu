import sys

import docker
from absl import app, flags, logging

FLAGS = flags.FLAGS


def main(argv, client):
    FLAGS(argv)
    cs = client.containers.list(all=True)
    for container in cs:
        print(container.id, container.name)
