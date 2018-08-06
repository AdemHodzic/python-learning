import unittest
from bikeRide import solution

class BikeRideTest(unittest.TestCase):
    
    def test_first(self):
        input = [240]
        output = 4
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [808]
        output = 14
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
