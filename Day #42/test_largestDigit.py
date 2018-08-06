import unittest
from largestDigit import solution

class LargestDigitTest(unittest.TestCase):

    def test_first(self):
        input = [2]
        output = 99 
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [3]
        output = 999
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
