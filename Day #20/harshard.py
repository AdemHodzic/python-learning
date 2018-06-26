

def main():
  print(firstTwenty())

def firstTwenty():
  arr = []

  number = 1000

  while len(arr) < 20:
    if isHarshard(number):
      arr.append(number)
    number += 1
  return arr

def isHarshard(number):
  strs = list(str(number))
  arr = []
  for c in strs:
    arr.append(int(c))
  
  return number % sum(arr) == 0

if __name__ == '__main__':
  main()