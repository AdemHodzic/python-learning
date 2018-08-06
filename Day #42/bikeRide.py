def solution(timer):
    result = ''
    result += str(timer / 60)
    result += str(timer % 60)
    return reduce(lambda x,y: x + int(y), result, 0)

