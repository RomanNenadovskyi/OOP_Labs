import unittest
from math_tool import MathTool

class TestMathTool(unittest.TestCase):

    def setUp(self):
        self.math = MathTool()

    def test_add(self):
        self.assertEqual(self.math.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.math.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.math.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.math.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.divide(10, 0)

if __name__ == "__main__":
    unittest.main()