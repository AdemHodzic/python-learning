def main():
    height = int(input('Enter the height of triangle: '))
    current = 1
    counter = 1
    while current < height:
        for i in range(0,counter):
            print(str(current) + ' ', end='')
            current += 1
        counter += 1
        print()
    



if __name__ == '__main__':
    main()