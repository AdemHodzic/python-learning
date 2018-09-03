from __future__ import division

def solution(number):
    return is_prime(number) and str(number) in str(float(1 / number))


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

print('Testing for 3')
assert solution(3) == True

print('Testing for 11')
assert solution(11) == False

print('All tests passed succesfully.')
