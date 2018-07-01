import unittest
from coinStairs import solution

class CoinStairsTest(unittest.TestCase):

    def test_first(self):
        input = 5
        output = 2
        result = solution(input)
        self.assertEqual(result,output)

    def test_second(self):
        input = 8
        output = 3
        result = solution(input)
        self.assertEqual(result,output)


if __name__ == '__main__':
    unittest.main()
