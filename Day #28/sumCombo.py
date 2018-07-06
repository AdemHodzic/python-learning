def solution(arr):
    max = len(arr)
    result = [0]
    while max > 0:
        for i in range(0, max):
            temp = arr[i:max]
            if sum(temp) > sum(result):
                result =  temp
        max -= 1
    return result
