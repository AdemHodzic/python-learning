def main():
    height = int(input("Enter the height of pipes in mario: "))
    while height < 0 or height > 23:
        height = int(input("Enter the height of pipes in mario: "))
    num_hash = 1
    for i in range(height,-1,-1):
        spaces = ' ' * i
        hashtags = '#' * num_hash
        print(spaces + hashtags + ' ' + hashtags)
        num_hash+=1

if __name__ == '__main__':
    main()