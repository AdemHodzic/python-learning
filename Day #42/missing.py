def solution(arr):
    return len(list(set(range(min(arr), max(arr)+1)) - set(arr)))
