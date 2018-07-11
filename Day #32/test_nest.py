import unittest
from nest import solution

class NestTest(unittest.TestCase):
    
    def test_first(self):
        input = [[5,4,0,3,1,6,2]]
        output = 4
        result = solution(*input)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
