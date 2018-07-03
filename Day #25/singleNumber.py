# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Input: [2,2,3,2]
# Output: 3

def solution(arr):
  for number in arr:
    if not arr.count(number) == 3:
      return number