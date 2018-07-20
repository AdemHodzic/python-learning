import unittest
from transpose import solution

class TransposeTest(unittest.TestCase):

    def test_first(self):
        input = [[[1,2,3],[4,5,6],[7,8,9]]]
        output = [[1,4,7],[2,5,8],[3,6,9]]
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[[1,2,3],[4,5,6]]]
        output = [[1,4],[2,5],[3,6]]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
