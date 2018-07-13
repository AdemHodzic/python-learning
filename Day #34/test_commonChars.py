import unittest
from commonChars import solution

class CommonCharsTest(unittest.TestCase):

    def test_first(self):
        input = ['aabcc', 'adcaa']
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['a', 'b']
        output = 0
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
