def main():
    digits = int(input('Enter the number of digits: '))
    print(largestPalindromeProduct(digits))

def largestPalindromeProduct(digits):
    palindrome = 0
    max = 10 ** digits - 1
    min = 10 ** (digits - 1)
    for i in range(max, min, -1):
        for j in range(i, min, -1):
            mult = i * j
            if isPalindrome(mult) and mult > palindrome:
                palindrome = mult
    return palindrome

def isPalindrome(number):
    string = str(number)
    max_index = len(string) - 1
    for i in range(0, len(string)):
        if not string[i] == string[max_index]:
            return False
        max_index -= 1
    return True


if __name__ == '__main__':
    main()