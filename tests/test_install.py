import os
import pytest
import tfgpu.install as install
from tfgpu.install import RUNFILE_PATH, BASHRC_PATH
from tfgpu.install import TFGPU_DOTFILE_PATH, TFGPU_SOURCE_STRING
from tfgpu.utils import line_exists_in_file, remove_line_from_file


def test_check_prerequisite():
    assert install.check_prerequisites()


def test_build_shell_command():
    if os.path.exists(TFGPU_DOTFILE_PATH):
        os.remove(TFGPU_DOTFILE_PATH)

    assert not os.path.exists(TFGPU_DOTFILE_PATH)
    install.build_shell_commands()
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
