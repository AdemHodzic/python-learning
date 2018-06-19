def main():
  string = raw_input('Enter yout string: ')
  print(correct(string))

def correct(string):
  arr = []
  arr.append(str.isupper(string))
  arr.append(str.islower(string))
  arr.append(firstCapital(string))

  for boolean in arr:
    if boolean:
      return boolean
  return False

def firstCapital(string):
  if not str.isupper(string[0]):
    return False
  for i in range(1, len(string)):
    if not str.islower(string[i]):
      return False
  return True

if __name__ == '__main__':
  main()