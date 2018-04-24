def main():
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))
    action = str(input("What do you want to do wit them ? "))

    if action=="sum":
        print(firstNumber + secondNumber)
    elif action=="dif":
        print(firstNumber - secondNumber)
    elif action=="mlp":
        print(firstNumber * secondNumber)
    elif action=="div":
        print(firstNumber / secondNumber)
    else:
        print("Invalid operation!")
        

if __name__ == "__main__":
    main()