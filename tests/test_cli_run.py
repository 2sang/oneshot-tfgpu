import pytest
import tfgpu.exceptions as exep

from tfgpu.app import Command


@pytest.fixture
def run_command():
    return Command(['run'])

@pytest.fixture
def run_command_with_default_image():
    return Command(['run', 'default'])


def test_raise_command_not_specified(run_command):
    with pytest.raises(exep.CommandNotSpecified):
        run_command.execute()
