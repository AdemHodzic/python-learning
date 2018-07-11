import unittest
from bounds import solution

class BoundsTest(unittest.TestCase):

    def test_first(self):
        input = [1,22]
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
