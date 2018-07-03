import unittest
from maxLine import solution

class MaxLineTest(unittest.TestCase):

  def test_first(self):
    input = [[1,1],[2,2],[3,3]]
    output = 3
    result = solution(input)
    self.assertEqual(result, output)

  def test_second(self):
    input = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    output = 4
    result = solution(input)
    self.assertEqual(result, output)


if __name__ == '__main__':
  unittest.main()