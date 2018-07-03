import unittest
from singleNumber import solution

class SingleNumberTest(unittest.TestCase):

  def test_first(self):
    input = [2,2,3,2]
    output = 3
    result = solution(input)
    self.assertEqual(result, output)

  def test_second(self):
      input = [0,1,0,1,0,1,99]
      output = 99
      result = solution(input)
      self.assertEqual(result, output)

if __name__ == '__main__':
  unittest.main()

  