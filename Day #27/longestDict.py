# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by 
# deleting some characters of the given string. If there are more than one possible results, 
# return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.

def solution(string, arr):
    result = ''
    for word in arr:
        if contains(string, word):
            if (len(word) == len(result) and word < result) or len(word) > len(result):
                result = word 
    return result

def contains(string, word):
    for char in word:
        if not string.count(char) >= word.count(char):
            return False
    return True
