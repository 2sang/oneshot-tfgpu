import sys
import logging

import docker
from absl import app, flags, logging

import tfgpu.exceptions as exep
import tfgpu.utils as utils

FLAGS = flags.FLAGS

flags.DEFINE_string("hello", None, "Your name")


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
    for config_key, question_string in questions.items():
        default_string = '(default: {}):'.format(default_config[config_key])
        answer = input(question_string + default_string)
        if not answer:
            new_config[config_key] = default_config[config_key]
        else:
            new_config[config_key] = answer


def main(cli_args, testmode=False):
    conf = utils.load_conf()
    if not initialized(conf) and not testmode:
        ask_init(conf)

    options = cli_args.options
    client = cli_args.client
    print("options: {}".format(options))
    FLAGS(cli_args.args)

    if not options:
        logging.warning("Specify image(tfgpu run [IMAGE_NAME])")
        logging.warning("To see available images: tfgpu image ls")
        raise exep.CommandTargetNotSpecified

    return True
