def solution(str1, str2):
    result = 0
    
    str1 = list(str1)
    str2 = list(str2)
    
    for i in range(0, len(str1)):
        current = str1[i]
        if current in str2:
            result += 1
            rem = str2.index(current)
            del str2[rem]
    return result
