def solution(down, up):
    
    arr = []

    for number in range(down, up + 1):
        if selfdiv(number):
            arr.append(number)
    
    return arr


def selfdiv(number):

    if str(number).count('0') > 0:
        return False

    for digit in str(number):
        if not number % int(digit) == 0:
            return False
    return True

