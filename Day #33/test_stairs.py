import unittest
from stairs import solution

class StairsTest(unittest.TestCase):

    def test_first(self):
        input = [26]
        output = 196418
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
