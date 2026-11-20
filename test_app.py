
import unittest
from app import calculate_total, calculate_discount


class TestApp(unittest.TestCase):

    def test_calculate_total(self):
        self.assertEqual(calculate_total(100, 2), 200)

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(200, 10), 180.0)


if __name__ == "__main__":
    unittest.main()
