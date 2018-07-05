# Given a string containing just the characters '(' and ')', find the length of the 
# longest valid (well-formed) parentheses substring. 

def solution(string):
    return string.count('()') * 2
