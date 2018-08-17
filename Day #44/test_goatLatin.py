import unittest
from goatLatin import solution

class GoatLatinTest(unittest.TestCase):
    def test_first(self):
        input = ['I speak Goat Latin']
        output = 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = ['The quick brown fox jumped over the lazy dog']
        output = 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa';
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
