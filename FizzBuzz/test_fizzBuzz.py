from fizzBuzz import fizz_buzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        self.listToAssert = fizz_buzz()
        self.assertEqual('FizzBuzz', self.listToAssert[14])



if __name__ == '__main__':
    unittest.main()