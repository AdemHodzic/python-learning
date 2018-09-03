def solution(number):
    primes = sieve(number)
    for i in primes:
        if number % i == 0 and number % i**2 == 0:
            return True
    return False

def sieve(number):
    arr = []
    for i in range(2, number + 1):
        if i not in arr:
            for j in range(i * i, number + 1, i):
                arr.append(j)
    return list(set(range(2, number + 1)) - set(arr))

print('Testing for 8')
assert solution(8) == True

print('Testing  for 50')
assert solution(50) == True

print('All test passed successfully')
