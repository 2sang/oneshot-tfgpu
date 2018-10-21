from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
import sys

import docker
import fire

import tfgpu.utils as utils

def print_usage():
    print("Usage: tfgpu <command> <options>")

def check_initialized():
    conf = utils.load_conf()
    return conf['general']['initialized']

def run_container(image):

def _run(image='default'):
    if not check_initialized():
        return _init()
    
    docker_client = docker.from_env()
    run_container(image)
    return True

def _ls():
    pass

def _commit():
    pass

def _init():
    return True

def _ps():
    pass

def _set():
    pass


def main():
    if len(sys.argv) == 1:
        print_usage()
        return False
    available_commands = ['run', 'ls', 'ps', 'set', 'init', 'commit']
    fire.Fire({command: eval('_' + command) for command in available_commands})

if __name__ == "__main__":
    main()
