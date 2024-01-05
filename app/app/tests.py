"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calculator


class CalcTests(SimpleTestCase):
    """Test the calculator module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calculator.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calculator.subtract(10, 15)

        self.assertEqual(res, 5)
