import unittest
from sum_of_divisiors import sum_of_divisors
from is_prime import is_prime
from prime_number_of_divisors import prime_number_of_divisors
from contains_digit import contains_digit
from contains_digits import contains_digits
from is_number_balanced import is_number_balanced
from count_substrings import count_substrings
from zero_insertion import zero_insert
from sum_matrix import sum_matrix
from matrix_bombing_plan import matrix_bombing_plan


class TheRealDealTest(unittest.TestCase):

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(1), 1)
        self.assertEqual(sum_of_divisors(8), 15)
        self.assertEqual(sum_of_divisors(16), 31)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(33))
        self.assertTrue(is_prime(37))
        self.assertFalse(is_prime(-10))

    def test_prime_number_of_divisors(self):
        self.assertFalse(prime_number_of_divisors(14))
        self.assertTrue(prime_number_of_divisors(9))
        self.assertTrue(prime_number_of_divisors(16))

    def test_contains_digit(self):
        self.assertFalse(contains_digit(908, 1))
        self.assertTrue(contains_digit(18951851, 8))
        self.assertFalse(contains_digit(1, 0))
        self.assertTrue(contains_digit(15, 5))

    def test_contains_digits(self):
        self.assertTrue(contains_digits(2420157142, [0, 2]))
        self.assertFalse(contains_digits(2141, [0]))
        self.assertFalse(contains_digits(1, [9]))
        self.assertTrue(contains_digits(441412698, [1, 4]))
        self.assertTrue(contains_digits(914081, [0, 8]))

    def test_is_number_balanced(self):
        self.assertFalse(is_number_balanced(1222222))
        self.assertTrue(is_number_balanced(1234510))
        self.assertFalse(is_number_balanced(14325400))

    def test_count_substrings(self):
        self.assertNotEqual(count_substrings("Pesho esho esh", "esh"), 2)
        self.assertEqual(count_substrings("Python Java", "a"), 2)
        self.assertEqual(count_substrings(" ident, part, in, space,", ","), 4)

    def test_zero_insert(self):
        self.assertEqual(zero_insert(5050055), 505000505)
        self.assertNotEqual(zero_insert(414414441), 41404140441)
        self.assertEqual(zero_insert(77773333), 707070703030303)

    def test_sum_matrix(self):
        self.assertEqual(sum_matrix([[111, 222, 111], [22, 11, 11], [2]]), 490)
        self.assertNotEqual(sum_matrix([[2, 3, 4], [3, 4, 5], [4, 5, 6]]), 35)
        self.assertEqual(sum_matrix([[1, 0, 1], [2, 1, 2], []]), 7)

    def test_matrix_bombing_plan(self):
        m = [[8, 9, 5], [4, 3, 2], [1, 2, 3]]
        result = {
            (0, 0): 22,
            (0, 1): 15,
            (0, 2): 27,
            (1, 0): 23,
            (1, 1): 17,
            (1, 2): 27,
            (2, 0): 34,
            (2, 1): 28,
            (2, 2): 30,
        }
        self.assertEqual(matrix_bombing_plan(m), result)

if __name__ == '__main__':
    unittest.main()
