import unittest
from goldbach import solution

class GoldbachTest(unittest.TestCase):

    def test_first(self):
        input = [11]
        output = [2,2,7]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [35]
        output = [2,2,31]
        result = solution(*input)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()
