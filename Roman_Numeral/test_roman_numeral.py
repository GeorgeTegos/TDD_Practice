from roman_numeral import RomanNumeral
import unittest

class TestRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumeral()
        self.number = 4423
        

    def test_return_string_from_roman_numerals(self):
        self.assertEqual('CM',self.roman_numerals.return_string_from_roman_numerals(900))

    def test_return_thousands_of_a_number(self):
        self.assertEqual('MMMM',self.roman_numerals.return_thousands_of_a_number(self.number))

    def test_return_hundreds_of_a_number(self):
        self.assertEqual('CD',self.roman_numerals.return_hundreds_of_a_number(self.number))

    def test_return_tens_of_a_number(self):
        self.assertEqual('XX',self.roman_numerals.return_tens_of_a_number(self.number))

    def test_return_units_of_a_number(self):
        self.assertEqual('I',self.roman_numerals.return_units_of_a_number(self.number))





if __name__ == '__main__':
    unittest.main()