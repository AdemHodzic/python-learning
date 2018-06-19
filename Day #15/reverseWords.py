from functools import reduce

def main():
  string = raw_input('Enter your sentence: ')
  print(reverse(string))

def reverse(string):
  arr = (string.split(' ')[::-1])
  return str(arr).join(' ')
if __name__ == '__main__':
  main()