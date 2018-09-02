def solution(number):
    digits =  sum(map(lambda x: int(x), list(str(number))))
    return is_prime(number) and is_prime(int(digits))


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3,number,2):
        if number % i == 0:
            return False
    return True

print('Testing for 113')
assert solution(113) == True
print('Testing for 89')
assert solution(89) == True
print('Testing for 19')
assert solution(19) == False


