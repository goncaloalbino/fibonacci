import unittest
from unittest.mock import patch

from api.fibonacci import (fibonacci, fibonacci_sequence, fibonacci_value,
                           fibonacci_values, blacklist_add, blacklist_remove)

FIBONACCI_VALUES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        fib = fibonacci()
        number = len(FIBONACCI_VALUES)
        fib_sequence = [next(fib) for _ in range(number)]

        self.assertEqual(fib_sequence, FIBONACCI_VALUES)

    def test_fibonacci_sequence(self):
        number = len(FIBONACCI_VALUES)
        fib_sequence = fibonacci_sequence(number)
        fib = {k: v for k, v in enumerate(FIBONACCI_VALUES, 1)}

        self.assertDictEqual(fib_sequence, fib)

    def test_fibonacci_value_valid_number(self):
        value_1 = fibonacci_value(2)
        value_2 = fibonacci_value(10)

        self.assertEqual(value_1[0], FIBONACCI_VALUES[1])
        self.assertEqual(value_1[1], 200)

        self.assertEqual(value_2[0], FIBONACCI_VALUES[9])
        self.assertEqual(value_2[1], 200)

    @patch('api.fibonacci.BLACKLIST', {2, 5})
    def test_fibonacci_value_blacklisted_number(self):
        value_1 = fibonacci_value(2)
        value_2 = fibonacci_value(5)

        self.assertIn(value_1[0], "Number 2 is blacklisted")
        self.assertEqual(value_1[1], 400)

        self.assertIn(value_2[0], "Number 5 is blacklisted")
        self.assertEqual(value_2[1], 400)

    def test_fibonacci_values(self):
        numbers = range(1, len(FIBONACCI_VALUES) + 1)
        fib_sequence1 = fibonacci_values(page=1, items_per_page=10)
        fib_sequence2 = fibonacci_values(page=2, items_per_page=5)
        fib_sequence3 = fibonacci_values(page=3, items_per_page=3)

        self.assertEqual(fib_sequence1[0], list(zip(numbers, FIBONACCI_VALUES)))
        self.assertEqual(fib_sequence2[0], list(zip(numbers[5:], FIBONACCI_VALUES[5:])))
        self.assertEqual(fib_sequence3[0], list(zip(numbers[6:9], FIBONACCI_VALUES[6:9])))
        self.assertEqual(fib_sequence3[1], 200)

    @patch('api.fibonacci.BLACKLIST', {2, 5})
    def test_fibonacci_values_blacklisted_numbers(self):
        items_per_page = 10
        blacklist_numbers = [2, 5]

        fib_sequence = fibonacci_values(page=1, items_per_page=items_per_page)
        sequence = fibonacci_sequence(items_per_page)
        for number in blacklist_numbers:
            del sequence[number]
        values = [(number, value) for number, value in sequence.items()]

        self.assertEqual(fib_sequence[0], values)
        self.assertEqual(fib_sequence[1], 200)

    @patch('api.fibonacci.BLACKLIST', set())
    def test_add_blacklist_number(self):
        from api.fibonacci import BLACKLIST
        number_1 = 5
        number_2 = 10

        blacklist_add(number_1)
        blacklist_add(number_2)
        result = blacklist_add(number_2)

        self.assertEqual(len(BLACKLIST), 2)
        self.assertEqual(BLACKLIST, {number_1, number_2})
        self.assertEqual(result[1], 200)
        self.assertIn(result[0],  f"Value {number_2} added to blacklist")

    def test_remove_blacklist_invalid_number(self):
        number = 5

        result = blacklist_remove(number)

        self.assertEqual(result[1], 400)
        self.assertIn(result[0],  f"Value {number} is not blacklisted")

    @patch('api.fibonacci.BLACKLIST', {5})
    def test_remove_blacklist_number(self):
        from api.fibonacci import BLACKLIST
        number = 5

        self.assertEqual(len(BLACKLIST), 1)

        result = blacklist_remove(number)

        self.assertEqual(result[1], 200)
        self.assertIn(result[0], f"Value {number} removed from blacklist")
        self.assertEqual(len(BLACKLIST), 0)
