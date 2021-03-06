# On the first row, we write a 0. Now in every subsequent row, we look at the previous 
# row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

# Examples:
# Input: N = 1, K = 1
# Output: 0

def solution(row, index):
  string = '0'
  for i in range(0,row - 1):
    new = ''
    for char in list(string):
      if char == '0':
        new += '01'
      else:
        new += '10'
    string = new
  return int(string[index - 1])