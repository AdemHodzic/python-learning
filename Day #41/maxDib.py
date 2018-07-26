def solution(divisor, number):
    return max(filter(lambda x: x % divisor == 0, range(1, number + 1)))
