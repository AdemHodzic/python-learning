from datetime import  datetime
from random import randint
from time import sleep

def isPrime(value):
    if value % 2 == 0:
        return False
    for i in range(3,value,2):
        if value % i == 0:
            return False
    return True

def main():
    for i in range(5):
        current_second = datetime.today().second
        if(isPrime(current_second)):
            print("This time is kinda odd")
        else:
            print("Work, work, work")
        sleep(randint(1,42))    

if __name__ == "__main__":
    main()