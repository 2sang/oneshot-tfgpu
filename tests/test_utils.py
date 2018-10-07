import subprocess

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


def test_available_tags():
    tags = utils.load_available_tags()
    assert type(tags) == list
    assert 'nightly-devel-py3' in tags
    assert 'latest' in tags
    assert '1.9.0-rc2-gpu-py3' in tags

