import pytest
import tfgpu.exceptions as exep

from tfgpu.app import Command


# TODO: factorize all commands with this fixture
@pytest.fixture
def make_command():
    def _make_command(command_name):
        return Command[command_name]
    return _make_command


@pytest.fixture
def run_command():
    return Command(['run'])


@pytest.fixture
def commit_command():
    return Command(['commit'])


@pytest.fixture
def ls_command():
    return Command(['ls'])


@pytest.fixture
def ps_command():
    return Command(['ps'])


@pytest.fixture
def set_command():
    return Command(['set'])


@pytest.fixture
def init_command():
    return Command(['init'])


class TestCommandClass:

    def test_run_command(self, run_command):
        assert run_command.module_filename == '_run.py'

    def test_commit_command(self, commit_command):
        assert commit_command.module_filename == '_commit.py'

    def test_set_command(self, set_command):
        assert set_command.module_filename == '_set.py'

    def test_ls_command(self, ls_command):
        assert ls_command.module_filename == '_ls.py'

    def test_init_command(self, init_command):
        assert init_command.module_filename == '_init.py'
