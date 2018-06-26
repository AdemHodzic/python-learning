

def main():
  print(fifth())



def fifth():
  number = 2
  while not solution(number):
    number += 1
  return number


def solution(number):
  strs = str(number)
  arr = []
  for c in strs:
    arr.append(int(c)**5)
  return number == sum(arr)

if __name__ == '__main__':
  main()