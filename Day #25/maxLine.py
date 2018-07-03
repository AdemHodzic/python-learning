# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4


def solution(arr):
  result = 0
  obj = {}

  
  if len(arr) == 1:
    return 1
  
  if len(arr) == 2:
    return 2

  for combo in arr:
    if combo[0] == combo[1]:
      if not 'same' in obj.keys():
        obj.update({'same' : 1})
      else:
        obj['same'] += 1

  for combo in arr:
    combo_sum = sum(combo)
    if not combo_sum in obj.keys():
      obj.update({combo_sum: 1})
    else:
      obj[combo_sum] += 1


  for value in obj.values():
    if value > result:
      result = value
  return result