import unittest
from longestStrings import solution

class LongestStringsTest(unittest.TestCase):

    def test_first(self):
        input = [["aba", "aa", "ad", "vcd", "aba"]]
        output =  ["aba", "vcd", "aba"]
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = [["abc",  "eeee",  "abcd",  "dcd"]]
        output = ["eeee",  "abcd"]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
