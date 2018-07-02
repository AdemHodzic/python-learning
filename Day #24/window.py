# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
def solution(main, sub):
  result = ''

  for i in range(0 , len(main) - len(sub)):
    counter = len(sub)
    temp = counter + i
    current = main[i:temp]

    while not contains(current, sub) :
      counter += 1
      temp = counter + i
      current = main[i:temp]
    
    if (len(current) < result or result == ''):
      result = current

  return result

def contains(main, sub):
  sub = list(sub)
  for char in sub:
    if not char in list(main):
      return False
  return True
