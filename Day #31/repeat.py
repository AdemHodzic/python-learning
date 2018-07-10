def solution(string):
    
    counter = len(string) - 1 
    current = string[0:counter]
    while len(current) > 1:
        if string.count(current) > 1:
            return True
        counter -= 1
        current = string[0:counter]

    return False
