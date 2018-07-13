def solution(number):
    number = list(str(number))
    half = int(len(number) / 2)
    a1 = map(lambda x: int(x), number[:half])
    a2 = map(lambda x: int(x), number[half:])

    return sum(a1) == sum(a2)
