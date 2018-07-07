import unittest
from prefix import solution

class PrefixTest(unittest.TestCase):

    def test_first(self):

        input = [ ['abc', 'abd', 'abbd'] ]
        output = 'ab'
        result = solution(*input)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
