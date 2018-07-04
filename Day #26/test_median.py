import unittest
from median import MedianFinder

class MedianTest(unittest.TestCase):

    def test_first(self):
        obj = MedianFinder()
        obj.addNum(1)
        obj.addNum(2)
        self.assertEqual(obj.findMedian(), 1.5)

    def test_second(self):
        obj = MedianFinder()
        obj.addNum(1)
        obj.addNum(2)
        obj.addNum(3)
        self.assertEqual(obj.findMedian(), 2)

if __name__ == '__main__':
    unittest.main()
