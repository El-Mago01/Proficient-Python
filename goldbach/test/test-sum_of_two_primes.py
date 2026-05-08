import pytest
from goldbach.goldbach import is_sum_of_two_primes

def test_is_sum_of_two_primes_true():
    assert is_sum_of_two_primes(4) == [(2, 2)]
    assert is_sum_of_two_primes(6) == [(3, 3)]
    assert is_sum_of_two_primes(8) == [(3, 5), (5, 3)]
    assert is_sum_of_two_primes(10) == [(3, 7), (5, 5), (7, 3)]
    assert is_sum_of_two_primes(12) == [(5, 7), (7, 5)]
    assert is_sum_of_two_primes(14) == [(3, 11), (7, 7), (11, 3)]
    assert is_sum_of_two_primes(100) == [(3, 97), (11, 89), (17, 83), (29, 71), (41,59), (47,53), (53, 47), (59, 41), (71, 29), (83, 17),
    (89,11), (97, 3)]

def test_is_sum_of_two_primes_false():
    assert is_sum_of_two_primes(1) == []
    assert is_sum_of_two_primes(2) == []
    assert is_sum_of_two_primes(3) == []
    assert is_sum_of_two_primes(5) == []
    assert is_sum_of_two_primes(7) == []
    assert is_sum_of_two_primes(9) == []
    assert is_sum_of_two_primes(11) == []
 
