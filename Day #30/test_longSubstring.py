import unittest
from longSubstring import solution

class LongSubstringTest(unittest.TestCase):

    def test_first(self):
        input = ['aaabb', 3]
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [ 'ababbc', 2 ]
        output = 4 
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
