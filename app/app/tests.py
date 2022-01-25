from django.test import TestCase
from app.calc import basic_calc, subtract

class CalcTests(TestCase):
    def test_basic_calc(self):
        self.assertEqual(basic_calc(3,8), 11)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract(11,5), 6)