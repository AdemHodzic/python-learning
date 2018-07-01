import unittest
from medians import solution

class MediansTest(unittest.TestCase):
    def test_first(self):
        nums1 = [1, 3]
        nums2 = [2]
        output = 2.0
        result =solution(nums1, nums2)
        self.assertEqual(result, output)

    def test_second(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        output = 2.5
        result = solution(nums1, nums2)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
