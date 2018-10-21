import subprocess
import os

import tfgpu.utils as utils


def test_load_conf():
    d = utils.load_conf()
    assert type(d) == dict


def test_update_conf():
    orig_yaml_path = 'conf.yaml'
    test_yaml_path = 'test_conf.yaml'

    pseudo_conf = utils.load_conf(orig_yaml_path)
    utils.update_conf(pseudo_conf, test_yaml_path)
    updated_conf = utils.load_conf(test_yaml_path)
    assert updated_conf == pseudo_conf
    os.remove(test_yaml_path)
    assert not os.path.exists(test_yaml_path)


def test_available_tags():
    tags_by_version = utils.load_available_tags_by_version()
    assert type(tags_by_version) == dict
    assert type(tags_by_version['latest']) == list
