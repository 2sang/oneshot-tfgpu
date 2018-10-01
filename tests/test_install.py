import os
import pytest
import tfgpu.install as install
from tfgpu.install import RUNPATH


def test_load_conf():
    d = install.load_conf()
    print("d: {}".format(d))
    assert type(d) == dict


def test_check_prerequisite():
    assert install.check_prerequisites()


def test_set_shell_command():
    assert not os.path.exists(os.path.expanduser('~/.tfgpu'))
    installed = install.set_shell_commands()
    assert installed
    assert os.path.exists('~/.tfgpu')
    with open(os.path.expanduser('~/.bashrc'), 'r') as tfgpu:
        lines = tfgpu.readlines()
        assert 'source ~/.tfgpu\n' in lines

    # Teardown
    os.remove('~/.tfgpu')
    lines.remove('source ~/.tfgpu\n')
    with open(os.path.expanduser('~/.bashrc'), 'w') as brc:
        for line in lines:
            brc.write(line)
