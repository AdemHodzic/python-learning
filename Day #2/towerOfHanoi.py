def main():
    number = int(input("Enter the number of rings: "))
    
    hanoi(number, 'a', 'b', 'c')

def hanoi(number, fromTower, toTower, helperTower):

    print(f"{fromTower}    {toTower}    {helperTower}")
    if number > 1:
        hanoi(number-1, fromTower, helperTower, toTower)
    
    if number > 1:
        hanoi(number-1, helperTower, toTower, fromTower)

if __name__ == "__main__":
    main()