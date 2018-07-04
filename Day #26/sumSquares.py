# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

from math import sqrt

def solution(number):
    
    for i in range(1, number):
        second = number - i**i
        if isPerfect(second):
            return True


    return False

def isPerfect(number):
    try:
        return sqrt(number) % 1 == 0
    except:
        return False
