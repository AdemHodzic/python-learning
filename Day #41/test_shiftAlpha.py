import unittest
from shiftAlpha import solution

class ShiftAlphaTest(unittest.TestCase):

    def test_first(self):
        input = ['crazy']
        output = 'dsbaz'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['aaaabbbccd']
        output = 'bbbbcccdde'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['fuzzy']
        output = 'gvaaz'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
