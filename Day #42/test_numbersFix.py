import unittest
from numbersFix import solution

class NumbersFixTest(unittest.TestCase):

    def test_first(self):
        input = [1234,2]
        output = '34'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [1234, 4]
        output = '1234'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = [1234, 5]
        output = '01234'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
