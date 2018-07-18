import unittest
from spellCheck import solution

class SpellCheckTest(unittest.TestCase):

    def test_first(self):
        input = ['a']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['zombie']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_third(self):
        input = ['transceiver']
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_fourth(self):
        input = ['veil']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

    def test_fifth(self):
        input = ['icier']
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
