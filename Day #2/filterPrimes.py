from itertools import chain

def main():
    value = int(input("input your numbers (input -1 for end)"))
    values = []
    while value >= 0:
        values.append(value)
        value = int(input())
    primeValues = list(filter(lambda x: isPrime(x), values))
    another_list = list(filter(lambda x: not x in primeValues, values))
    print(list(chain(primeValues,another_list)))

def isPrime(num):
    if(num%2==0):
        return False
    for i in range(3,num,2):
        if num % i == 0:
            return False
    return True



if __name__ == "__main__":
    main()