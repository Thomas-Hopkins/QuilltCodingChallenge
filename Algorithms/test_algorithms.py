from . import algorithms
from itertools import permutations
import random
import string

def test_permutations_original_input():
    test_input = "hat\nabc\nZu6"
    for line in test_input.splitlines():
        expected_out = ["".join(per) for per in permutations(line, len(line))]
        expected_out.sort()
        
        actual_out = algorithms.permutations(line)

        assert actual_out == expected_out

def test_permutations_variable_length_strings():
    MAX_LEN = 5 # Higher numbers take much more time
    MIN_LEN = 0
    possible_chars = string.ascii_letters + string.digits

    # Test 100 random variable length strings
    for _ in range(100):
        line = "".join(random.choice(possible_chars) for _ in range(random.randint(MIN_LEN, MAX_LEN)))
        expected_out = ["".join(per) for per in permutations(line, len(line))]
        expected_out.sort()
        
        actual_out = algorithms.permutations(line)

        assert actual_out == expected_out
