# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 4, 3, 2, 1, 0]

def main():
  string = "loveleetcode"
  char = 'e'

  print(distance(string, char))

def distance(string, char):

  arr = []
  for i in range(0, len(string)):
    counter = 0
    for j in range(i,len(string)):
      if string[j] == char:
        break
      else:
        counter += 1
    arr.append(counter)

  return arr




if __name__ == '__main__':
  main()