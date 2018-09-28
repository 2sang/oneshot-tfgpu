import pytest
import sys
print("sys.path: {}".format(sys.path))
from oneshottf import bootstrap as bs

def test_load_config():
    conf = bs.load_config()
    assert type(conf) == dict
    
def test_check_requirements():
    assert bs.check_requirements()
