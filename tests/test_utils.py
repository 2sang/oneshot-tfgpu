import subprocess

import tfgpu.utils as utils
import tfgpu.install as install
from tfgpu.install import TFGPU_DOTFILE_PATH


def test_load_conf():
    d = utils.load_conf()
    print("d: {}".format(d))
    assert type(d) == dict
