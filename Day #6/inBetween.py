def main():
    begin = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    arr = list(range(begin, end+1))
    for num in arr:
        if num % 2 == 1 and num % 3 == 0:
            print(num)

if __name__ == '__main__':
    main()