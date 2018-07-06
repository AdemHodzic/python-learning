import unittest
from twice import solution

class TwiceTest(unittest.TestCase):

    def test_first(self):
        input = [[3,6,1,0]]
        output = 1
        result = solution(*input)
        self.assertEqual(result, output)

    
    def test_second(self):
        input = [[1,2,3,4]]
        output = -1
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
