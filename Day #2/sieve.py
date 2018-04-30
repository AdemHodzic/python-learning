def main():
    value = int(input("Enter number at the end: "))
    primesList = tryFilter(value+1)
    print(primesList)

def calculate(value):
    temp = list(range(2,value))
    for i in temp:
        temp = list(filter(lambda x: x == i or not x % i == 0, temp))
    return temp

   
if __name__ == "__main__":
    main()

