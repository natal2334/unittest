import pytest
from calc_lean import add

def test_method1():
    assert add(3,5) == 8

def test_method2():
    assert add(15,5) == 21

@pytest.mark.xfail #xfail as test doesn't pass
def test_method3():
    assert add(3,5) == 9

@pytest.mark.skip #skip test
def test_function1():
    assert add(15,5) == 20

def test_function2():
    assert add(-1,1) == 0
