## Given a list of non negative integers, arrange them such that they form the largest number.
## Input: [3,30,34,5,9]
## Output: "9534330"

from fractions import Fraction

def main():
  arr = []
  number = int(input('Enter your numbers or enter 0 or less to quit: '))
  while number > 0:
    arr.append(number)
    number = int(input('Enter your numbers or enter 0 or less to quit: '))

  print(calculateNumber(arr))

def calculateNumber(arr):
  new_arr = sorted(arr, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
  solution = ''
  for num in new_arr:
    solution += str(num)
  return int(solution)

if __name__ == '__main__':
  main()