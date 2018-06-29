# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def main():
  print(selfDividing(1,22))

def selfDividing(min,max):
  arr = []
  
  for number in range(min, max + 1):
    if correct(number):
      arr.append(number)

  return arr


def correct(num):
  if str(num).count('0') > 0:
    return False

  for char in str(num):
    current = int(char)
    if not num % current == 0:
      return False

  return True

if __name__ == '__main__':
  main()