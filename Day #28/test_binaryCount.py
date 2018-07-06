import unittest
from binaryCount import solution

class BinaryCountTest(unittest.TestCase):

    def test_first(self):
        input = [5]
        output = [0,1,1,2,1,2]
        result = solution(*input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
