def main():
    size = int(input("Enter the size of matrix: "))
    matrix = list()
    for i in range(0,size):
        matrix.append(list())
    i = 0
    for row in matrix:
        for i in range(0,size):
            temp = int(input())
            row.append(temp)

    for row in matrix:
        for col in row:
            print(col)
        print('\n')

if __name__ == "__main__":
    main()