import unittest
from missingPositive import solution

class MissingPositiveTest(unittest.TestCase):

    def test_first(self):
        input = [[1,2,0]]
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[3,4,-1,1]]
        output = 2         
        result = solution(*input)         
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
