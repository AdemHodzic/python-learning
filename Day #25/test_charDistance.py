import unittest
from charDistance import solution


class CharDistanceTest(unittest.TestCase):
  def test_first(self):
    input_string = 'loveleetcode'
    input_char = 'e'
    output = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    result = solution(input_string, input_char)
    self.assertEqual(result, output)

if __name__ == '__main__':
  unittest.main()