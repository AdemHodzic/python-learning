# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

def solution(string, char):
  arr = []
  counter = 0
  for i,c in enumerate(string):
    if c == char:
      arr.append(i)
  
  temp = []
  for i,c in enumerate(string):
    min_list = []
    for elem in arr:
      min_list.append(abs(i - elem))
    temp.append(min(min_list))

  return temp