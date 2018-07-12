import unittest
from morse import solution

class MorseTest(unittest.TestCase):

    def test_first(self):
        input = [["gin", "zen", "gig", "msg"]]
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
