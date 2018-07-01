import unittest
from jumps import solution

class JumpsTest(unittest.TestCase):

    def test_first(self):
        input = [2,3,1,1,4]
        output = True
        result = solution(input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [3,2,1,0,4]
        output = False
        result = solution(input)
        self.assertEqual(result, output)


if __name__== '__main__':
    unittest.main()
