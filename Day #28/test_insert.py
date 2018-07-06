import unittest
from insert import solution

class InsertTest(unittest.TestCase):

    def test_first(self):
        input = [[1,3,5,6], 5]
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[1,3,5,6], 2]
        output =  1
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = [[1,3,5,6], 7]
        output = 4 
        result =solution(*input)
        self.assertEqual(result, output)

    def test_fourth(self):
        input = [[1,3,5,6], 0]
        output = 0
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
