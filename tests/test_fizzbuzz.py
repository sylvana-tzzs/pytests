import pytest

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n

@pytest.mark.parametrize("input_val,expected", [
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (7, 7)
])
def test_fizzbuzz(input_val, expected):
    assert fizzbuzz(input_val) == expected