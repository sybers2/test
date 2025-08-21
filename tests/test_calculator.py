import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1, 0)


if __name__ == "__main__":
    unittest.main()
