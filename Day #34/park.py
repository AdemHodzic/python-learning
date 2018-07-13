def solution(arr):
    ppl = list(filter(lambda x: x > 0, arr))

    result = []

    for i in range(0, len(arr)):
        if arr[i] == -1:
            result.append(-1)
        else:
            result.append(min(ppl))
            ppl.remove(min(ppl))
    return result
