def solution(number):
    return is_prime(number) and is_power_two(number + 1)

def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3,number,2):
        if number % i == 0:
            return False

    return True

def is_power_two(number):
    if number == 1:
        return True
    elif not number % 2 == 0:
        return False
    else:
        return is_power_two(number / 2)


print('Testing for solution(3)')
assert solution(3) == True
print('Testing for solution(31)')
assert solution(31) == True
print('Testing for solution(17)')
assert solution(17) == False
print('All tests passed succesfully!')
