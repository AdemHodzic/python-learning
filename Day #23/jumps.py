def solution(arr):
    if len(arr) == 1:
        return True

    max = arr[0]

    for i in range(0, len(arr)):

        if max <= i and arr[i] == 0:
            return False

        if i + arr[i] > max:
            max= i + arr[i]

        if max >= len(arr):
            return True
    
    return False
