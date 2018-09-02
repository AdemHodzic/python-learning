def solution(number):
    for _  in range(30):
        number = make_palindrome(number)
        if is_palindrome(number):
            return True
    return False

def make_palindrome(number):
    return number + int(str(number)[::-1])

def is_palindrome(number):
    return str(number) == str(number)[::-1]

print('Testing for 12')
assert solution(12) == True


print('Testing for 57 ')
assert solution(57) == True


print('Testing for 10911 ')
assert solution(10911) == False






