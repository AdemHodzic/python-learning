import unittest
from anagrams import solution

class AnagramsTest(unittest.TestCase):

    def test_first(self):
        input = ['cbaebabacd', 'abc']
        output = [0, 6]
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['abab', 'ab']
        output = [0,1,2]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
