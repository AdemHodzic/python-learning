def solution(string):

    current = 0
    
    result = ''
    
    copy = string[:]

    for index, char in enumerate(string):

        if char.isupper():
            result += (string[current:index]).lower()
            result += ' ' 
            current = index
        
        if index == len(string) - 1:
            result += (string[current:index]).lower()
            result += (string[::-1])[0].lower()

    return result.strip()
