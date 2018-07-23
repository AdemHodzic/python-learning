import unittest
from match import solution


class MatchTest(unittest.TestCase):

    def test_first(self):
        input = ["abcde", ["a", "bb", "acd", "ace"]]
        output = 3
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
