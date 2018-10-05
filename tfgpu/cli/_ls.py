import sys

import docker
from absl import app, flags, logging

FLAGS = flags.FLAGS


def main(argv, client):
    FLAGS(argv)
    cs = client.containers.list(all=True)
    if not cs:
        print("No container running.")
        return;
    print("CID  image\tcontainer_nickname")
    for container in cs:
        print(container.id[:4], container.image, container.name)
