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


# HARDCODED web scrapying script, should refactor somehow..
def load_tags_from_dockerhub(url):
    available_tags = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    m1 = list(soup.body.div.main.children)[1]
    m2 = list(m1.children)[1]
    m3 = list(m2.children)[1]
    m4 = m3.div.div.div.div
    m5 = list(m4.children)[1:]
    for m in m5:
        available_tags.append(m.div.contents[0])
    return available_tags


def load_available_tags_by_version():
    available_tags = load_tags_from_dockerhub(tensorflow_repository_url)
    version_strings = {tag.split('-')[0] for tag in available_tags}
    available_tags_by_version = {version: [] for version in version_strings}
    for tag in available_tags:
        available_tags_by_version[tag.split('-')[0]].append(tag)
    return available_tags_by_version


def print_usage():
    print("Usage: tfgpu <command> <options>")
