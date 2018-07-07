def solution(arr):

    temp = min(arr)
    result = ''
    for i in range(1, len(temp)):
        current = temp[0:i]
        if not allStartWith(arr, current):
            return current[0:i-1]
    return result


def allStartWith(arr, string):
    for word in arr:
        if not string in word:
            return False

    return True
