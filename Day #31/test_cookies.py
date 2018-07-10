import unittest
from cookies import solution

class CookiesTest(unittest.TestCase):

    def test_first(self):
        input = [[1,2,3], [1,1]]
        output = 1
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [[1,2], [1,2,3]]
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
