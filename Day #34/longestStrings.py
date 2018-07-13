def solution(arr):
    max_len = len(max(arr, key=lambda x: len(x)))
    return [x for x in arr if len(x) == max_len]
