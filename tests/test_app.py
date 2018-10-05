import pytest
import tfgpu.exceptions as exep

from tfgpu.app import Command


@pytest.fixture
def run_command():
    return Command(['run'])

@pytest.fixture
def commit_command():
    return Command(['commit'])

class TestCommandClass:

    def test_run_command(self, run_command):
        assert run_command.module_filename == '_run.py'

    def test_commit_command(self, commit_command):
        assert commit_command.module_filename == '_commit.py'
    
    def test_raise_wrong_command_name_exception(self):
        with pytest.raises(exep.NoSuchCommand):
            Command(['Cool']).execute()
