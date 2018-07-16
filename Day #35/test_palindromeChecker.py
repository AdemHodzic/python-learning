import unittest
from palindromeChecker import solution

class PalindromeCheckerTest(unittest.TestCase):

    def test_first(self):
        input = ['aabb']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['zyyzzzzz']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
