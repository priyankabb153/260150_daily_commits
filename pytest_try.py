import pytest


def check(x,y):
    return x+y


def test_method():
    assert check(2,3) >= 0
    assert check(2,3) == 10