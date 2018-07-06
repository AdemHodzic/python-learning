import unittest
from largeGroups import solution

class LargeGroupsTest(unittest.TestCase):

    def test_first(self):
        input = ['abbxxxxzzy']
        output = [[3,6]]
        result = solution(*input)
        self.assertEqual(result, output)
    
    def test_second(self):
        input = ['abc']
        output = []
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
