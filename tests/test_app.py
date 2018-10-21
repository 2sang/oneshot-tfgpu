import unittest.mock as mock

import tfgpu.app as app
import tfgpu.exceptions as exep
import docker
import pytest


def test_run():
    assert app.execute('run')
