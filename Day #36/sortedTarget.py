def solution(arr, target):
    if target in arr:
        return [arr.index(target), arr.index(target) + arr.count(target) - 1]
    else:
        return [-1,-1]
