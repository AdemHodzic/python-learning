import unittest
from twoSum import solution


class TwoSumTest(unittest.TestCase):

    def test_first(self):
        input = [[2, 7, 11, 15], 9]
        output = sorted([0,1])
        result = solution(*input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
