def main():
    arr = [1,2,3,4,5,6]
    number = int(input('Enter your number: '))
    print(solution(arr,number))

def solution(arr,number):
    arr.reverse()
    print(arr)
    for i in arr:
        if number == 0:
            break
        if i <= number:
            number -= i
            print(number)
    return (number == 0)


if __name__ == '__main__':
    main()