import unittest
from luckyTicket import solution

class LuckyTicketTest(unittest.TestCase):

    def test_first(self):
        input = [1230]
        output = True
        result = solution(*input)
        self.assertEqual(result, output)

    def test_second(self):
        input = [239017]
        output = False
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
