import subprocess

import tfgpu.utils as utils


def test_load_conf():
    d = utils.load_conf()
    print("d: {}".format(d))
    assert type(d) == dict

def test_available_tags():
    tags = utils.load_available_tags()
    assert type(tags) == list
