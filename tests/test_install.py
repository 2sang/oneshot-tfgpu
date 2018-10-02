import os
import pytest
import tfgpu.install as install
from tfgpu.install import RUNFILE_PATH, BASHRC_PATH, TFGPU_DOTFILE_PATH
from tfgpu.utils import line_exists_in_file, remove_line_from_file

TFGPU_SOURCE_STRING = 'source ' + TFGPU_DOTFILE_PATH + '\n'


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
    install.set_shell_commands()
    assert os.path.exists(TFGPU_DOTFILE_PATH)
    assert line_exists_in_file(BASHRC_PATH, TFGPU_SOURCE_STRING)


def test_teardown_shell_command():
    # Teardown
    assert os.path.exists(TFGPU_DOTFILE_PATH)
    assert line_exists_in_file(BASHRC_PATH, TFGPU_SOURCE_STRING)

    os.remove(TFGPU_DOTFILE_PATH)
    assert not os.path.exists(TFGPU_DOTFILE_PATH)
    if remove_line_from_file(BASHRC_PATH, TFGPU_SOURCE_STRING):
        assert not line_exists_in_file(BASHRC_PATH, TFGPU_SOURCE_STRING)
