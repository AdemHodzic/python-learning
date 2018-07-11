def solution(arr, string):
    result = []    
    string = string.split(' ')
    
    for word in string:
        result.append(replace(word, arr))
    return ' '.join(result)

def replace(word, arr):
    for elem in arr:
        if elem in word:
            return elem
    return word
            

