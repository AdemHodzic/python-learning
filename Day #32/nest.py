def solution(arr):

    results = []

    for elem in arr:
        index = elem
        temp = []
        temp.append(index)
        while arr[index] not in temp:
            index = arr[index]
            temp.append(index)
        results.append(temp)        
    return len(max(results, key=lambda x:len(x)))
