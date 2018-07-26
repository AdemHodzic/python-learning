import unittest
from maxDib import solution

class MaxDibTest(unittest.TestCase):

    def test_first(self):
        input = [3,10]
        output = 9
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
