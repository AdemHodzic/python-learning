import unittest
from tandem import solution

class TandemTest(unittest.TestCase):

    def test_first(self):
        input = ['tandemtandem']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['qqq']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['qqqq']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_fourth(self):
        input = ['2w2ww']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
