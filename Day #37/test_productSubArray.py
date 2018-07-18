import unittest
from productSubArray import solution

class ProductSubArrayTest(unittest.TestCase):

    def test_first(self):
        input = [[2,3,-2,4]]
        output = 6
        result = solution(*input)
        self.assertEqual(result,output)
    
    def test_second(self):
        input = [[-2, 0, -1]]
        output = 0
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
