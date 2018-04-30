def main():
    arr = list(range(1,101))
    for number in arr:
        if number % 5 == 0 and number % 3 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

if __name__ == "__main__":
    main()