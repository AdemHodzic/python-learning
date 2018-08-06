import unittest
from launchSequence import solution

class LaunchSequenceTest(unittest.TestCase):

    def test_first(self):
        input = [ ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"],  [1, 10, 11, 2, 12, 111]]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [["stage_1", "stage_1", "stage_2", "dragon"],  [2, 1, 12, 111]]
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
