import os
import pytest
import tfgpu.install as install
from tfgpu.install import RUNFILE_PATH, BASHRC_PATH, TFGPU_DOTFILE_PATH


def test_load_conf():
    d = install.load_conf()
    print("d: {}".format(d))
    assert type(d) == dict


def test_check_prerequisite():
    assert install.check_prerequisites()


def test_set_shell_command():
    if os.path.exists(TFGPU_DOTFILE_PATH):
        os.remove(TFGPU_DOTFILE_PATH)

    assert not os.path.exists(TFGPU_DOTFILE_PATH)
    installed = install.set_shell_commands()
    assert installed
    with open(BASHRC_PATH, 'r') as tfgpu:
        lines = tfgpu.readlines()
        assert 'source ' + TFGPU_DOTFILE_PATH + '\n' in lines

    # Teardown
    os.remove(TFGPU_DOTFILE_PATH)
    assert not os.path.exists(TFGPU_DOTFILE_PATH)
    lines.remove('source ' + TFGPU_DOTFILE_PATH + '\n')
    with open(BASHRC_PATH, 'w') as brc:
        for line in lines:
            brc.write(line)
