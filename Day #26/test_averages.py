import unittest
from averages import solution

class AveragerTest(unittest.TestCase):

    def test_first(self):
        input = [ [9,1,2,3,9], 3 ]
        output = 20
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
