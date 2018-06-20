"""
Given a List of words, return the words that can be 
typed using letters of alphabet on only one row's of American
keyboard like the image below.

https://leetcode.com/static/images/problemset/keyboard.png
"""

def main():
  word = raw_input('Enter your word (enter blank to stop): ')
  arr = []
  while word:
    arr.append(word)
    word = raw_input('Enter your word (enter blank to stop): ')
  print(canBeWrittenOnKeyboard(arr))

def canBeWrittenOnKeyboard(words):
  first_row = ['q', 'w','e', 'r','t', 'y','u', 'i','o', 'p',]  
  second_row = ['a', 's','d', 'f','g', 'h','j', 'k','l']  
  third_row = ['z', 'x','c', 'v','b', 'n','m',]

  arr = []

  for word in words:
    if check_row(word, first_row) or check_row(word, second_row) or check_row(word,third_row):
      arr.append(word)
  
  return arr

def check_row(word, arr):
  for char in word:
    if not str.lower(char) in arr:
      return False
  return True

if __name__ == '__main__':
  main()