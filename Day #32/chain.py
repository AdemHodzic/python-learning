def solution(arr):
    arr = map(lambda x: sum(x), arr)
    counter = 1
    current = min(arr)
    while current + 4 in arr:
        counter += 1
        current += 4
    return counter
