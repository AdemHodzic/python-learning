def main():
    string = str(input('Enter your string: '))
    arr = {}
    distinct_chars = 0
    for char in string:
        if not contains(arr,char):
            arr[char] = 1
            distinct_chars += 1
        else:
            arr[char] = arr[char] + 1
    if is_string_prime(arr) and is_prime(len(string)):
        print('prime')
    else:
        print('not prime')
    

def contains(arr, char):
    for i in arr.keys():
        if i == char:
            return True
    return False

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def is_string_prime(map):
    for k,v in map.items():
        if not is_prime(v):
            return False
    return True

if __name__ == '__main__':
    main()