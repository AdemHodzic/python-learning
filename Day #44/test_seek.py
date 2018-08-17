import unittest
from seek import solution

class SeekTest(unittest.TestCase):

    def test_first(self):
        input = ['abcd', [0,2], ["ab","ec"],["eee","ffff"]]
        output = 'eeecd'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['abcd', [0,2], ["a","cd"],["eee","ffff"]]
        output = 'eeebffff'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
