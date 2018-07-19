def solution(arr):
    
    for i in range(0,len(arr)):
        temp = arr[i]
        temp = temp[::-1]
        arr[i] = temp
    
    
    for a in arr:
        for i in range(0, len(a)):
            if a[i] == 0:
                a[i] = 1
            else:
                a[i] = 0

    return arr
