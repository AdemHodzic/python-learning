import unittest
from chessColor import solution

class ChessColorTest(unittest.TestCase):

    def test_first(self):
        input = ['A1', 'C3']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['A1', 'H3']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['B3', 'H8']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
