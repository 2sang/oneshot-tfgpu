import sys
import pytest
from oneshottf import bootstrap as bs

print("sys.path: {}".format(sys.path))

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
    
def test_check_requirements():
    assert bs.check_requirements()
