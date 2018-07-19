def solution(front, back):
    result = float('inf')
    another = float('inf')
    maximum = len(front) * 2
    for i in range(0, maximum):
        temp = front[i//2]
        if temp not in back and temp < result:
            result = temp
        front, back = back, front
    if result == another:
        return 0
    else:
        return result
