import pytest
from src.prime_checker import prime_checker

@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])

def test_is_prime(num,expected):
    assert prime_checker(num)==expected