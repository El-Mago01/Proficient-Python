import pytest
from goldbach.goldbach import is_prime

def test_is_prime_true():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(11) == True
    

def test_is_prime_false():
    assert is_prime(4) == False
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False    
    assert is_prime(123) == False

