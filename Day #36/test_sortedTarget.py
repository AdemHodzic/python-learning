import unittest
from sortedTarget import solution

class SortedTargetTest(unittest.TestCase):

    def test_first(self):
        input = [[5,7,7,8,8,10], 8]
        output = [3,4]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [[5,7,7,8,8,10], 6]
        output = [-1,-1]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
