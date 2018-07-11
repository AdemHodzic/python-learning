import unittest
from myCalendar import MyCalendar

class MyCalendarTest(unittest.TestCase):
    def test_first(self):
        calendar = MyCalendar()
        
        input = [10,20]
        output = True
        result = calendar.book(*input)
        self.assertEqual(result, output)

        input = [15,25]
        output = False
        result = calendar.book(*input)
        self.assertEqual(result, output)

        input = [20, 30]
        output = True
        result = calendar.book(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()

