import unittest
from binarySymbol import solution

class BinarySymbolTest(unittest.TestCase):

  def test_first(self):
    input_row = 1
    input_index = 1
    output = 0
    result = solution(input_row, input_index)
    self.assertEqual(result, output)

  def test_second(self):
    input_row = 2
    input_index = 1
    output = 0
    result = solution(input_row, input_index)
    self.assertEqual(result, output)

  def test_third(self):
      input_row = 2
      input_index = 2
      output = 1
      result = solution(input_row, input_index)
      self.assertEqual(result, output)

  def test_fourth(self):
      input_row = 4
      input_index = 5
      output = 1
      result = solution(input_row, input_index)
      self.assertEqual(result, output)



if __name__ == '__main__':
  unittest.main()