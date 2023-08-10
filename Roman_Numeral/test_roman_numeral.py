from roman_numeral import RomanNumeral
import unittest

class TestRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumeral()
        self.number = 4423

    def test_find_thousands(self):
        self.assertEqual('MMMM',self.roman_numerals.find_thousands(self.number))





if __name__ == '__main__':
    unittest.main()