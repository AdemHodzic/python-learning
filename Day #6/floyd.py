def main():
    rows = int(input("Enter the number of rows in  triangle: "))
    number = sum(list(range(1,rows+1)))
    while rows > 0:
        for i in range(0,rows):
            print(number, end=" ")
            number-=1
        rows-=1
        print()

if __name__ == '__main__':
    main()