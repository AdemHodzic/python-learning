import unittest
from subsequence import solution

class SubsequenceTest(unittest.TestCase):

    def test_first(self):
        input = [ 'ahbgdc', 'abc' ]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['ahbgdc', 'axc']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
