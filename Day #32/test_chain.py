import unittest
from chain import solution

class ChainTest(unittest.TestCase):

    def test_first(self):
        input = [[[1,2], [2,3], [3,4]]]
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
