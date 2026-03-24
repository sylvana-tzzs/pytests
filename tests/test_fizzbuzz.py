import pytest

def fizz_buzz(nums):
    return [
        "FizzBuzz" if n % 3 == 0 and n % 5 == 0 else
        "Fizz" if n % 3 == 0 else
        "Buzz" if n % 5 == 0 else
        n
        for n in nums
    ]

def test_fizz_buzz():
    nums = list(range(1, 16))
    expected = [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz"]
    assert fizz_buzz(nums) == expected