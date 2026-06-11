import unittest
from parameterized import parameterized
from utils import check_even

class TestCheckEven(unittest.TestCase):

    @parameterized.expand([
        ("positive_even", 2, True),
        ("positive_odd", 3, False),
        ("zero", 0, True),
        ("negative_even", -4, True),
        ("negative_odd", -5, False),
    ])
    def test_check_even(self, name, number, expected):
        self.assertEqual(check_even(number), expected)

if __name__ == "__main__":
    unittest.main()