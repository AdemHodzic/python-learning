import unittest
from primePalindrome import solution

class PrimePalindromeTest(unittest.TestCase):

    def test_first(self):
        input = [6]
        output = 7
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [8]         
        output = 11         
        result = solution(*input)         
        self.assertEqual(result, output)

    def test_third(self):
        input = [13]
        output = 101
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
