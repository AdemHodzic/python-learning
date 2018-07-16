import unittest
from hotelSum import solution

class HotelSumTest(unittest.TestCase):

    def test_first(self):
        input = [[[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]]
        output = 9
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[[1,1,1],  [2,2,2],  [3,3,3]]]
        output = 18
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
