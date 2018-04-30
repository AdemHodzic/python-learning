def main():
    coins = [25,10,5,1]
    bill = float(input())
    bill *= 100
    result = 0
    for coin in coins:
        if bill < coin:
            continue 
        while bill >= coin:
            bill-=coin
            result+=1
    print(result)

if __name__ == '__main__':
    main()