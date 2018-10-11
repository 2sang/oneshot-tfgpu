import unittest.mock as mock

import tfgpu.app as app
import tfgpu.exceptions as exep
import docker
import pytest


@pytest.fixture
def docker_client():
    return docker.from_env()

@pytest.fixture(autouse=True)

def test_cli_arguments_class(docker_client):
    cc = app.CliArguments(['_run.py', '-a'], docker_client)
    assert cc.module_filename == '_run.py'
    assert cc.options == ['-a']


