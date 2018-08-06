import unittest
from missing import solution

class MissingTest(unittest.TestCase):
    
    def test_first(self):
        input = [[6, 2, 3, 8]]
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
