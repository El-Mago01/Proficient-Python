import pytest
from goldbach.goldbach import cleanup

def test_cleanup_even_list():
    assert cleanup([(1, 2), (2, 1)]) == [(1, 2)]

    

def test_cleanup_odd_list():
    assert cleanup([(1, 2), (2, 1), (3, 4)]) == [(1, 2), (3, 4)]

