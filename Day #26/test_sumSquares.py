import unittest
from sumSquares import solution

class SumSquaresTest(unittest.TestCase):

    def test_first(self):
        input = [5]
        output = True
        result = solution(*input)
        self.assertEqual(output, result)
    
    def test_second(self):
        input = [3]
        output = False
        result = solution(*input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
