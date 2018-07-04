import unittest
from combos import solution

class CombosTest(unittest.TestCase):

    def test_first(self):
        input = [4,2]
        output = sorted([[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],])
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
