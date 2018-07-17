import unittest
from sumBinary import solution

class SumBinaryTest(unittest.TestCase):

    def test_first(self):
        input = ['11', '1']
        output = '100'
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['1010','1011']
        output = '10101'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
