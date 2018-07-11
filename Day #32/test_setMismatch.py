import unittest
from setMismatch import solution

class SetMismatchTest(unittest.TestCase):

    def test_first(self):
        input = [[1,2,2,4]]
        output = [2,3]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
