from functools import reduce

def main():
  min = int(input('enter min number:'))
  max = int(input('enter max number:'))
  print(scm(min,max))

def scm(min,max):
  arr = range(min,max+1)
  mult = reduce(lambda x,y: x * y, arr,1)
  solution = mult
  
  while mult > min:
    if divisible(mult, arr):
      solution = mult
    mult -= 1
  return solution

def divisible(mult, arr):
  for num in arr:
    if not mult % num == 0:
      return False
  return True


if __name__ == '__main__':
  main()