def solution(number):
    temp = number + 1
    while True:
        if isPrime(temp) and str(temp) == (str(temp))[::-1]:
            return temp
        temp += 1

def isPrime(number):
    if number % 2 == 0:
        return False

    for i in range(3,number,2):
        if number % i == 0:
            return False
    return True
