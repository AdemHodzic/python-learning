def solution(arr):
    head = 0
    tail = head + 3
    for i in range(0, len(arr) - 2):
        temp = arr[head:tail]
        if pattern(temp):
            return True
        head += 1
        tail = head + 3
    return False

def pattern(arr):
    return max(arr) == arr[1] and min(arr) == arr[0]
