def solution(arr):

    result = []

    for number in arr:
        if arr.count(number) > 1:
            result.append(number)
            break
    compare = set(range(1, max(arr) + 1))
    arr = set(arr)

    result.append(list(compare - arr)[0])

    return result
