from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import docker
import yaml
from subprocess


def check_prerequisites():
    # tfgpu dependencies(pip2, pip3)

    # nvidia driver dependencies

    return True


def load_conf(yaml_path='./conf.yaml'):
    with open(yaml_path, 'r') as f:
        return yaml.load(f)


def set_shell_commands():
    with open('~/.tfgpu', 'w') as tfgpu:
        tfgpu.write('alias tfgpu="python3 ' + os.path.realpath(__file__) + '"')
    with open('~/.bashrc', 'a') as brc:
        brc.write('source ')
    call(['source', '~/.bashrc'])


def install():
    if os.path.exists('~/.tfgpu'):
        return True
    set_shell_commands()


def main():
    # Todo: Sanity check for --runtime=nvidia option Mon 01 Oct 2018
    if not (check_prerequisites()):
        print("prerequisites not satistied")
        return

    conf = load_conf('conf.yaml')
    install()


class PrerequisiteNotSatisfied(Exception):
    pass


if __name__ == "__main__":
    main()
