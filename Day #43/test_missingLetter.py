import unittest
from missingLetter import solution

class MissingLetterChallenge(unittest.TestCase):

    def test_first(self):
        input = ['abce']
        output = 'd'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['abcdefghjklmno']
        output = 'i'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['abcdefghijklmnopqrstuvwxyz']
        output = ''
        result = solution(*input)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()
