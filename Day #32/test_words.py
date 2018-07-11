import unittest
from words import solution

class WordsTest(unittest.TestCase):

    def test_first(self):
        input = [["cat", "bat", "rat"], "the cattle was rattled by the battery"]
        output = "the cat was rat by the bat"
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
