def solution(arr):
    new_arr = []
    maximum = len(arr[0])
    for i in range(0, maximum):
        temp  = []
        for j in range(0, len(arr)):
            temp.append(arr[j][i])
        new_arr.append(temp)
    return new_arr
