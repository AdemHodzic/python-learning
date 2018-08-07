import unittest
from bananaCoins import solution

class BananaCoinsTest(unittest.TestCase):

    def test_first(self):
        input = [[1, 2, 10], 28]
        output = 6
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
