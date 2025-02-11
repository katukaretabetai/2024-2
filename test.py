import unittest
from calc_mul import calc

class TestCalc(unittest.TestCase):
    
    def test_valid_1(self):
        self.assertEqual(calc(1, 1), 1)

    def test_valid_2(self):
        self.assertEqual(calc(5, 10), 50)

    def test_valid_3(self):
        self.assertEqual(calc(10, 5), 50)

    def test_valid_4(self):
        self.assertEqual(calc(500, 500), 250000)

    def test_valid_5(self):
        self.assertEqual(calc(999, 999), 998001)

    def test_invalid_range_low(self):
        self.assertEqual(calc(0, 1), -1)

    def test_invalid_range_b_low(self):
        self.assertEqual(calc(1, 0), -1)

    def test_invalid_range_high(self):
        self.assertEqual(calc(1000, 1), -1)

    def test_invalid_range_b_high(self):
        self.assertEqual(calc(1, 1000), -1)

    def test_invalid_non_integer_a(self):
        self.assertEqual(calc(1.5, 2), -1)

    def test_invalid_non_integer_b(self):
        self.assertEqual(calc(2, 1.5), -1)

    def test_invalid_string_a(self):
        self.assertEqual(calc("a", 5), -1)

    def test_invalid_string_b(self):
        self.assertEqual(calc(10, "x"), -1)

    def test_invalid_string_c(self):
        self.assertEqual(calc("1a", 5), -1)

    def test_invalid_string_d(self):
        self.assertEqual(calc(10, "1x"), -1)

    def test_invalid_negative_a(self):
        self.assertEqual(calc(-5, 10), -1)

    def test_invalid_negative_b(self):
        self.assertEqual(calc(10, -5), -1)

