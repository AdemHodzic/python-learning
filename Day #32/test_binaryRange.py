import unittest
from binaryRange import solution

class BinaryRangeTest(unittest.TestCase):

    def test_first(self):
        input = [5]
        output = 4 
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
