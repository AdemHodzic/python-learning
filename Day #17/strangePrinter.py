## There is a strange printer with the following two special requirements:

## The printer can only print a sequence of the same character each time.
## At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
## Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it

def main():
  string = raw_input('Enter your string: ')
  print(numOfCycles(string))

def numOfCycles(string):
  
  total = 0
  arr = []
  
  for char in string:
    if not char in arr:
      arr.append(char)
      total += 1

  return total

if __name__ == '__main__':
  main()