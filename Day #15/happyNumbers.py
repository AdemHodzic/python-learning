from functools import reduce

def main():
  number = int(input('Enter yout number: '))
  print(isHappy(number))

def isHappy(number):
  string = str(number)
  counter = 0
  while counter < 1000:
    arr = []
    for digit in string:
      arr.append(int(digit)**2)
    sum = reduce( lambda x,y: x + y ,arr ,0)
    if sum == 1:
      return True
    else:
      string = str(sum)
      counter += 1
  return False

if __name__ == '__main__':
  main()