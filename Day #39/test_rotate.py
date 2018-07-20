import unittest
from rotate import solution

class RotateTest(unittest.TestCase):
    
    def test_first(self):
        input = [[1,2,3,4,5,6,7], 3]
        output = [5,6,7,1,2,3,4]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [[-1,-100,3,99], 2]
        output = [3,99,-1,-100]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
