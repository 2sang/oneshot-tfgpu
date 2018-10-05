import tfgpu.app as app
import tfgpu.exceptions as exep
import docker
import pytest


@pytest.fixture
def docker_client():
    return docker.from_env()


def test_cli_arguments_class(docker_client):
    cc = app.CliArguments(['_run.py', '-a'], docker_client)
    assert cc.module_filename == '_run.py'
    assert cc.options == ['-a']


def test_empty_constructor_raises_command_not_specified_exception():
    with pytest.raises(exep.CommandNotSpecified):
        app.Command()


def test_wrong_command_invokes_no_such_command_exception():
    with pytest.raises(exep.NoSuchCommand):
        app.Command(['you'])


def test_app_execute_function_returns_result():
    assert app.Command(['run']).execute() is True
