import unittest
from isLucky import solution

class IsLuckyTest(unittest.TestCase):

    def test_first(self):
        input = [134008]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [11]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = [100000]
        output = False
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
