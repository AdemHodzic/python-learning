import unittest
from rotate import solution

class RotateTest(unittest.TestCase):

    def test_first(self):
        input = [10]
        output = 4
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
