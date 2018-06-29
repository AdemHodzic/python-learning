# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
# You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".

def main():
  arr = ["abcw","baz","foo","bar","xtfn","abcdef"]
  print(solution(arr))

def solution(arr):

  max_product = 0

  for word in arr:
    for second_word in arr:
      if second_word == word:
        continue
      if mulipliable(word, second_word):
        number = len(word) * len(second_word)
        if number > max_product :
          max_product = number

  return max_product
  

def mulipliable(str1, str2):
  for char in str1:
    if not str2.find(char) == -1:
      return False
  return True


if __name__ == '__main__':
  main()