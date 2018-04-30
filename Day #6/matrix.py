from random import randint
def main():
    arr = [list(), list(), list(), list(), list()]
    for array in arr:
        for i in range(0,3):
            number = randint(20,31)
            array.append(number)
    
    for array in arr:
        for i in range(0,3):
            print(array[i])
if __name__ == '__main__':
    main()