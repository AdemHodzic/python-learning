import unittest
from kthInMatrix import solution

class kthInMatrixtest(unittest.TestCase):

  def test_first(self):
    input_arr =  [ [ 1,  5,  9], [10, 11, 13], [12, 13, 15] ]
    input_index = 8
    output = 13
    result = solution(input_arr, input_index)
    self.assertEqual(result, output)


if __name__ == '__main__':
  unittest.main()