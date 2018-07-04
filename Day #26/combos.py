# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

from itertools import combinations

def solution(n,k):
    arr = sorted(list(combinations(range(1, n+1), k)))
    return map(lambda x: list(x), arr)
