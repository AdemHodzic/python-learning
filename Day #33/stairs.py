def solution(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2

    result = 0
    prev = 1
    next = 2

    for i in range(2, number):
        result = prev + next
        prev = next
        next = result
    return result
