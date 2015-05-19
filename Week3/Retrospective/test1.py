import unittest
from factorial import factorial
from fibonacci import fibonacci
from sum_of_digits import sum_of_digits
from fac_digits import fact_digits
from palindrome import palindrome
from to_digits import to_digits
from to_number import to_number
from fib_number import fib_number
from count_vowels import count_vowels
from count_consonants import count_consonants
from char_histogram import char_histogram
from palindrome_score import p_score
from is_increasing import is_increasing
from is_decreasing import is_decreasing
from hack_numbers import next_hack


class WarmupsTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(8), [1, 1, 2, 3, 5, 8, 13, 21])

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(11), 2)
        self.assertEqual(sum_of_digits(1314), 9)
        self.assertEqual(sum_of_digits(0), 0)

    def test_fact_digits(self):
        self.assertEqual(fact_digits(1), 1)
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(31), 7)

    def test_palindrome(self):
        self.assertTrue(palindrome(121))
        self.assertFalse(palindrome(223))
        self.assertEqual(palindrome("kapak"), True)
        self.assertEqual(palindrome("baba"), False)

    def test_to_digits(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(1), [1])
        self.assertEqual(to_digits(12451451), [1, 2, 4, 5, 1, 4, 5, 1])

    def test_to_number(self):
        self.assertEqual(to_number([1, 0, 1]), 101)
        self.assertEqual(to_number([0, 0, 1]), 1)
        self.assertEqual(to_number([9, 9, 0, 9]), 9909)
        self.assertEqual(to_number([1, 2, 3]), 123)

    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)
        self.assertEqual(fib_number(5), 11235)
        self.assertEqual(fib_number(7), 11235813)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Dog and Cat"), 3)
        self.assertEqual(count_vowels("Python is awesome language"), 11)
        self.assertEqual(count_vowels("Cwm"), 0)

    def test_count_consonats(self):
        self.assertEqual(count_consonants("Java"), 2)
        self.assertEqual(count_consonants("Water, coffe, tea, cola"), 9)
        self.assertEqual(count_consonants("HackBulgaria"), 7)

    def test_char_histogram(self):
        self.assertEqual(char_histogram("Bree"), {"B": 1, "r": 1, "e": 2})
        self.assertEqual(char_histogram("HeY"), {"H": 1, "Y": 1, "e": 1})
        self.assertEqual(char_histogram(""), {})

    def test_p_score(self):
        self.assertEqual(p_score(1), 1)
        self.assertEqual(p_score(48), 3)
        self.assertEqual(p_score(198), 6)
        self.assertEqual(p_score(132), 2)

    def test_is_increasing(self):
        self.assertTrue(is_increasing([2, 3, 4]))
        self.assertFalse(is_increasing([102, 101, 99]))
        self.assertTrue(is_increasing([1, 1, 1, 2]))
        self.assertTrue(is_increasing([1000, 1001, 1002, 1003, 1004, 1005]))

    def test_is_decreasing(self):
        self.assertFalse(is_decreasing([2, 3, 4]))
        self.assertTrue(is_decreasing([102, 101, 99]))
        self.assertFalse(is_decreasing([2, 1, 0, 2]))
        self.assertTrue(is_decreasing([1000, 999, 500, 200, 100, 50]))

    def test_next_hack(self):
        self.assertEqual(next_hack(1), 7)
        self.assertEqual(next_hack(0), 1)
        self.assertEqual(next_hack(8032), 8191)

if __name__ == '__main__':
    unittest.main()
