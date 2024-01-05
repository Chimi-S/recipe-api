"""Sample Test"""

from django.test import SimpleTestCase

from app import calculator

class CalculateTest(SimpleTestCase):
    
    def test_add_numbers(self):

        res = calculator.add(5, 6)

        self.assertEqual(res, 11)