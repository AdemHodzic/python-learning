def solution(arr, target):
    
    if target < arr[0]:
        return 0
    
    if target >= arr[len(arr) - 1]:
        return len(arr)

    for i in range(1, len(arr)):
        prev = arr[i - 1]
        next = arr[i]
        if prev < target and target <= next:
            return i
    return -1
