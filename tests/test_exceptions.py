import pytest
import tfgpu.app as app
import tfgpu.exceptions as exep

from tfgpu.app import Command


def test_raise_wrong_command_name_exception():
    with pytest.raises(exep.NoSuchCommand):
        Command(['Cool']).execute()


def test_empty_constructor_raises_command_not_specified_exception():
    with pytest.raises(exep.CommandNotSpecified):
        app.Command()


def test_raise_command_target_not_specified():
    with pytest.raises(exep.CommandTargetNotSpecified):
        Command(['run']).execute()

    with pytest.raises(exep.CommandTargetNotSpecified):
        Command(['run', '--name=hi']).execute()


def test_wrong_command_invokes_no_such_command_exception():
    with pytest.raises(exep.NoSuchCommand):
        app.Command(['you'])
