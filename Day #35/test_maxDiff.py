import unittest
from maxDiff import solution

class MaxDiffTest(unittest.TestCase):

    def test_first(self):
        input = [[2, 4, 1, 0]]
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [[-1, 4, 10, 3, -2]]
        output = 7
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
