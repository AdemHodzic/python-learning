import unittest
from sumCombo import solution

class SumComboTest(unittest.TestCase):

    def test_first(self):
        input = [[-2,1,-3,4,-1,2,1,-5,4]]
        output = [4, -1,2,1]
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
