# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find median of two lists

# Example
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

from math import floor

def solution(nums1,nums2):
    arr = [*nums1, *nums2]
    arr.sort()
    return find_median(arr)


def find_median(arr):

    if len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 0:
        index = int(len(arr) / 2)
        return (arr[index] + arr[index - 1]) / 2
    else:
        index = floor(len(arr) / 2)
        return arr[index]
