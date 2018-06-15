def main():
    first = '12,13,15,19,212,556,2146'
    second = '13,44,12,432,788,2146,2145,46'

    first_arr = first.split(',')
    second_arr = second.split(',')

    solution = []

    for i in first_arr:
        if not second_arr.count(i) == 0:
            solution.append(i)

    print(solution)

if __name__ == '__main__':
    main()