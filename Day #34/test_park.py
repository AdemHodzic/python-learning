import unittest
from park import solution

class ParkTest(unittest.TestCase):

    def test_first(self):
        input = [[-1, 150, 190, 170, -1, -1, 160, 180]]
        output = [-1, 150, 160, 170, -1, -1, 180, 190]
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[-1, -1, -1, -1, -1]]
        output = [-1, -1, -1, -1, -1]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = [[4, 2, 9, 11, 2, 16]]
        output = [2, 2, 4, 9, 11, 16]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
