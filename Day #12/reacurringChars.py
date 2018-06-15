def main():
    string = str(input('Enter your string: '))
    print(firstRecurringCharacter(string))

def firstRecurringCharacter(string):
    for char in string:
        if string.count(char) > 1:
            return char
    return 'None'

if __name__ == '__main__':
    main()