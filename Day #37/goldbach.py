def solution(number):
    return sorted(compose(number))
def compose(number):
    arr = primes(number)
    arr = arr[::-1] 
    for i in arr:
        if (number - i) / 2 in arr:
            return [(number - i)/2, i, (number - i ) /2]        
    return [-1,-1]
def primes(number):
    
    arr = []
    for i in range(1, number):
        if isPrime(i):
            arr.append(i)
    return arr

def isPrime(number):
    if number == 1 or number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False
    
    for i in range(3, number, 2):
        if number % i == 0:
            return False
   
    return True
