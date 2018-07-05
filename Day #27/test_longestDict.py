import unittest
from longestDict import solution

class LongestDictTest(unittest.TestCase):

    def test_first(self):
        input = [ 'abpcplea', ["ale","apple","monkey","plea"] ]
        output = 'apple'
        result = solution(*input)
        self.assertEqual(output, result)
    
    def test_second(self):
        input = ['abpcplea', ["a","b","c"]]
        output = 'a'
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
