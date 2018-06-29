# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] 
# are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some 
# number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

# Input: [1,7,4,9,2,5]
# Output: 6
# The entire sequence is a wiggle sequence.

def main():
  arr = [1,7,4,9,2,5]
  print(calculateWiggle(arr))


def calculateWiggle(arr):
  wiggle = []

  for i in range(1, len(arr)):
    number = arr[i] - arr[i-1]
    wiggle.append(number)
  
  return countWiggle(wiggle)


def countWiggle(arr):
  counter = 0
  if arr[0] > 0:
    for i in range(1,len(arr)):
      if i % 2 == 0 and arr[i] > 0:
        counter += 1
      elif not i % 2 == 0 and arr[i] < 0:
        counter += 1
      else:
        break
    counter += 2
  else:
    for i in range(1,len(arr)):
      if not i % 2 == 0 and arr[i] > 0:
        counter += 1
      elif  i % 2 == 0 and arr[i] < 0:
        counter += 1
      else:
        break
    counter += 1
  return counter


if __name__ == '__main__':
  main()