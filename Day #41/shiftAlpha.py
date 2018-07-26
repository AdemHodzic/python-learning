def solution(string):
    result = ['' for i in string]
    for i,c in enumerate(string):
        if c == 'z':
            result[i] = 'a'
            continue
        result[i] = chr(ord(c) + 1)
    return ''.join(result)
