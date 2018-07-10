
def solution(string):
    arr = []
    arr.append(string)
    arr.extend(list(string))
    counter = 2
    
    result = 0

    while counter < len(string):
    
        for i in range(0, len(string) - counter + 1):
            temp = string[i:i + counter]
            arr.append(temp)
        
        counter += 1

    for combo in arr:
        if unique(combo):
            result += len(combo)
    
    return result
    
def unique(string):
    for char in string:
        if string.count(char) > 1:
            return False
    return True
