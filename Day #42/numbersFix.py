def solution(number, length):
    number = str(number)
    if length == len(number):
        return number
    elif length < len(number):
        number = number[::-1]
        return (number[:length])[::-1]
    else:
        zeros = '0' * (length - len(number))
        return zeros + number

