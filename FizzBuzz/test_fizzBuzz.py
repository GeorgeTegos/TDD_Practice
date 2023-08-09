from fizzBuzz import fizz_buzz
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        self.listToAssert = []
        for number in range(1,100):
            if (number % 3 == 0) and (number % 5 == 0):
                textToPrint = 'FizzBuzz'
                print(textToPrint)
                self.listToAssert.append(textToPrint)
            elif number % 3 == 0:
                textToPrint = 'Fizz'
                print(textToPrint)
                self.listToAssert.append(textToPrint)
            elif number % 5 == 0:
                textToPrint = 'Buzz'
                print(textToPrint)
                self.listToAssert.append(textToPrint)
            else:
                textToPrint = number
                print(textToPrint)
                self.listToAssert.append(textToPrint)

        self.assertEqual('FizzBuzz', self.listToAssert[14])



if __name__ == '__main__':
    unittest.main()