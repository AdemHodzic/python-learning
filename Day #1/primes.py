def primes(start, end):
    for i in range(start, end):
        if is_prime(i):
            yield i
        
def is_prime(num):
    if num%2==0:
        return False
    for i in range(3,num,2):
        if num%i==0:
            return False
    return True

def main():
    start = int(input("Enter a number for beggining: "))
    end = int(input("Enter a number for end: "))
    for num in primes(start, end):
        print(num)


if __name__ == "__main__":
    main()