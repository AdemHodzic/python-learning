import unittest
from uniLetters import solution

class UniLettersTest(unittest.TestCase):

    def test_first(self):
        input = ['ABC']
        output = 10
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['ABA']
        output = 7 
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
