import subprocess

import tfgpu.utils as utils


def test_load_conf():
    d = utils.load_conf()
    print("d: {}".format(d))
    assert type(d) == dict
