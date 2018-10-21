from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import glob
import logging
import sys

import docker
import fire
from PyInquirer import prompt

from tfgpu.prompt_styles import custom_style_1, custom_style_2, custom_style_3
import tfgpu.utils as utils


__version__ = '0.0.1'

PY3 = sys.version_info[0] >= 3

def print_usage():
    print("Usage: tfgpu <command> <options>")

def check_initialized():
    conf = utils.load_conf()
    return conf['general']['initialized']

def run_container(image):
    pass

def _run(image='default'):
    if not check_initialized():
        return True
        #return _init()
    
    docker_client = docker.from_env()
    run_container(image)
    return True

def _ls():
    pass

def _commit():
    pass

def ask_tag():
    print("Load all available tags from Dockerhub, please wait...")
    available_tags_by_version = utils.load_available_tags_by_version()
    select_version = [{
        'type': 'list',
        'name': 'version',
        'message': 'Choose tensorflow image version you want to run:',
        'choices': sorted(available_tags_by_version.keys(), reverse=True)
    }]
    answer = prompt(select_version, style=custom_style_1)
    version = answer['version']

    select_tag = [{
        'type': 'list',
        'name': 'tag',
        'message': 'Choose specified tag:',
        'choices': sorted(available_tags_by_version[version], reverse=True)
    }]
    answer = prompt(select_tag, style=custom_style_1)
    return answer['tag']

def _init():
    selected_tag = ask_tag()
    questions = [
        {
            'type': 'input',
            'name': 'mount_path',
            'message': 'path for mounting docker volume on your local filesystem?',
            'default': 'tfgpu_volume'
        },
        {
            'type': 'input',
            'name': 'volume_name',
            'message': 'name of the docker volume for mounting?',
            'default': 'tfgpu_volume'
        },
    ]
    answer = prompt(questions, style=custom_style_1)
    return True

    """
    {
        'tag': 'Tag?',
        'attached_volume': 'Name of the docker volume to mount?',
        'host_mountpath': 'Host mountpath?',
        'container_mountpath': 'Container mountpath?',
        'local_port': 'local port to access notebook?',
        'jupyter_port': 'notebook port?'
    }

    default_config = conf['images']['default']
    new_config = {}
    utils.update_conf()
    """

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
