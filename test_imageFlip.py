import unittest
from imageFlip import solution

class ImageFlipTest(unittest.TestCase):

    def test_first(self):
        input = [[[1,1,0],[1,0,1],[0,0,0]]]
        output = [[1,0,0],[0,1,0],[1,1,1]]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]]
        output = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
