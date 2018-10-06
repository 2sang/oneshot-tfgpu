import pytest
import tfgpu.exceptions as exep

from tfgpu.app import Command


@pytest.fixture
def run_command():
    return Command(['run'])


def test_raise_command_not_specified(self, run_command):
    with pytest.raises(exep.CommandNotSpecified):
        run_command.execute()

