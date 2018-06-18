from itertools import permutations

def main():
  string = str(raw_input('Enter your string: '))
  print(noRepeats(string))

def noRepeats(string):
  perms = list(permutations(string))
  counter = 0
  for element in perms:
    if unique(element):
      counter += 1
  return counter

def unique(element):
  for i in range(1,len(element)):
    if element[i] == element[i-1]:
      return False
  return True

if __name__ == '__main__':
  main()