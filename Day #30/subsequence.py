def solution(string, sub):
    counter = 0
    sub = list(sub)
    for char in string:
        if char == sub[counter]:
            counter += 1
    
    
    return counter == len(sub)
