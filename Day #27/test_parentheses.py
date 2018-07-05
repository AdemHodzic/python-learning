import unittest
from parentheses import solution

class ParenthesisTest(unittest.TestCase):

    def test_first(self):
        input = ['(()']
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)
    def test_second(self):
        input = [')()())']
        output = 4
        result = solution(*input)
        self.assertEqual(result, output)
 
if __name__ == '__main__':
    unittest.main()
