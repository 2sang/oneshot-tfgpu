import sys
import logging

import docker

import tfgpu.exceptions as exep
import tfgpu.utils as utils


def initialized(conf):
    return False


def ask_init(conf):

    questions = {
        'tag': 'Tag?',
        'attached_volume': 'Name of the docker volume to mount?',
        'host_mountpath': 'Host mountpath?',
        'container_mountpath': 'Container mountpath?',
        'local_port': 'local port to access notebook?',
        'jupyter_port': 'notebook port?'
    }

    default_config = conf['images']['default']
    new_config = {}


def main(cli_args=None, testmode=False):
    if not cli_args:
        print("run default container")
        return True
    conf = utils.load_conf()
    """
    if not initialized(conf) and not testmode:
        ask_init(conf)
    return True
    """
    return True
