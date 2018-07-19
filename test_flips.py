import unittest
from flips import solution

class FlipsTest(unittest.TestCase):

    def test_first(self):
        input = [ [1,2,4,4,7], [1,3,4,1,3]]
        output = 2
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
