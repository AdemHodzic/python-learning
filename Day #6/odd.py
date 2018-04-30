def main():
    number = int(input("Enter the number: "))
    result = 1
    string = str(number)
    for char in string:
        num = int(char)
        if num % 2 == 1:
            result *= num
    print(f"Result is {result}" )

if __name__ == '__main__':
    main()