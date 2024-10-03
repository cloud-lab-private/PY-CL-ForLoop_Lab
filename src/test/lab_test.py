import unittest
from src.main.lab import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()
