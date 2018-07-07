import unittest
from reverseInt import solution

class ReverseIntTest(unittest.TestCase):

    def test_first(self):
        input = [42]
        output = 24
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
