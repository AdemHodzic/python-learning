import unittest
from window import solution

class WindowTest(unittest.TestCase):
  def test_first(self):
    input_main = 'ADOBECODEBANC'
    input_sub = 'ABC'
    output = 'BANC'
    result = solution(input_main, input_sub)
    self.assertEqual(result, output)


if __name__ == '__main__':
  unittest.main()