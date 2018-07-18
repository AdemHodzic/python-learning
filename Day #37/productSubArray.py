def solution(arr):

    results = []
    num = 1
    result = float('-inf')
    while num < len(arr):
        for i in range(len(arr) - num + 1):
            temp = arr[i:i+num]
            results.append(temp)
        num += 1

    for i in results:
        temp = int(reduce(lambda x,y: x*y, i, 1))
        if temp > result:
            result = temp
    
    return result
