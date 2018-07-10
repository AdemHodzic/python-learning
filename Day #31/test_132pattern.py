import unittest
from pattern import solution

class patternTest(unittest.TestCase):

    def test_first(self):
        input = [[1,2,3,4]]
        output = False
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[3,1,4,2]]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = [[-1, 3, 2, 0]]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
