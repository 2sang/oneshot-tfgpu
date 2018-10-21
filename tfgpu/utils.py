import glob
import os
from os.path import dirname, basename, isfile
import subprocess

import yaml
import requests
from bs4 import BeautifulSoup

tensorflow_repository_url =\
    'https://hub.docker.com/r/tensorflow/tensorflow/tags/'

init_questions = {
    'tag': 'Tag?',
    'attached_volume': 'Name of the docker volume to mount?',
    'host_mountpath': 'Host mountpath?',
    'container_mountpath': 'Container mountpath?',
    'local_port': 'local port to access notebook?',
    'jupyter_port': 'notebook port?'
}

# Script from https://stackoverflow.com/questions/7040592/calling-the-source-
# command-from-subprocess-popen/12708396
def shell_source(script_path):
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    pipe = subprocess.Popen(". %s; env" % script_path,
                            stdout=subprocess.PIPE, shell=True)
    output = pipe.communicate()[0].decode('utf-8')
    env = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(env)


def line_exists_in_file(filepath, line):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return line in lines


def remove_line_from_file(filepath, line):
    if not os.path.exists(filepath):
        print("No such file: {}".format(filepath))
        return False

    # Read lines, remove target string from file
    with open(filepath, 'r') as f:
        lines = f.readlines()
        if line in lines:
            lines.remove(line)
        else:
            return False

    # Rewrite file
    with open(filepath, 'w') as f:
        for line in lines:
            f.write(line)
    return True


def load_conf(yaml_path='./conf.yaml'):
    with open(yaml_path, 'r') as f:
        return dict(yaml.load(f))


def update_conf(config_dict, yaml_path='./conf.yaml'):
    with open(yaml_path, 'w') as f:
        yaml.dump(config_dict, f, default_flow_style=False)


def load_modules_dict():
    module_names = glob.glob(dirname(__file__) + "/cli/*.py")
    modules_dict = {basename(f)[1:-3]: basename(f)[:-3]
                    for f in module_names
                    if isfile(f) and not f.endswith('__init__.py')}
    return modules_dict


# HARDCODED web scrapying script, should refactor somehow..
def load_available_tags():
    available_tags = []
    page = requests.get(tensorflow_repository_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    m1 = list(soup.body.div.main.children)[1]
    m2 = list(m1.children)[1]
    m3 = list(m2.children)[1]
    m4 = m3.div.div.div.div
    m5 = list(m4.children)[1:]
    for m in m5:
        available_tags.append(m.div.contents[0])
    return available_tags
