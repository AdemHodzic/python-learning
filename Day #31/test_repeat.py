import unittest
from repeat import solution

class RepeatTest(unittest.TestCase):

    def test_first(self):
        input = ['abab']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['aba']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['abcabcabcabc']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
