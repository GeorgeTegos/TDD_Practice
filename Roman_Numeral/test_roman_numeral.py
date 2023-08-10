from roman_numeral import RomanNumeral
import unittest

class TestRomanNumeral(unittest.TestCase):

    def setUp(self):
        self.roman_numerals = RomanNumeral()
        self.number = 3423

    def test_find_thousands(self):
        self.assertEqual(4,self.roman_numerals.find_thousands(self.number))





if __name__ == '__main__':
    unittest.main()