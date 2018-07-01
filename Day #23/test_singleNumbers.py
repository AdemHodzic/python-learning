import unittest
from singleNumbers import solution

class singleNumbersTest(unittest.TestCase):
    def test_first(self):
        input =  [1,2,1,3,2,5]
        output = [3,5]
        result = solution(input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
