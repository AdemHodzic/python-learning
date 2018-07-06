def solution(arr):
    arr = sorted(arr)
    filtered = list(filter(lambda x: x > 0  ,arr))
    temp =  range(min(filtered), max(filtered) + 1)
    
    for i in temp:
        if i not in arr:
            return i

    return max(temp) + 1
