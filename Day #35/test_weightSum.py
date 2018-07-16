import unittest
from weightSum import solution

class WeightSumTest(unittest.TestCase):

    def test_first(self):
        input = [[50, 60, 60, 45, 70]]
        output = [180, 105]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [[100, 51, 50, 100]]
        output = [150, 151]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
