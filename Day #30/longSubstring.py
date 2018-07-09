def solution(string, number):
    current = string[:number]
    for i in range(number + 1, len(string)):
        chars =  set(current)
        if returnable(current, chars, number):
            return len(current)
        current = string[:i]
    return 0

def returnable(current,chars,number):

    for char in chars:
        if current.count(char) < number:
            return False
    return True
