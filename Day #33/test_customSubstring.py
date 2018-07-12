import unittest
from customSubstring import solution

class CustomSubstringTest(unittest.TestCase):

    def test_first(self):
        input = ['CodefightsIsAwesome', 'IA']
        output = -1
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['sst', 'st']
        output = 1
        result = solution(*input)
        self.assertEqual(result, output)
if __name__ == '__main__':
    unittest.main()
