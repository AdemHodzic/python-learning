def solution(number):
    result = 0

    for number in range(0, number + 1):
        binary = bin(number)[2:]
        if correct(binary):
            result += 1

    return result

def correct(string):
    current = string[0]

    for char in string[1:]:
        if char == current:
            return False
        else:
            current = switch(current)
    return True


def switch(string):
    if string == '0':
        return '1'
    else:
        return '0'
