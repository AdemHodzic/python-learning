def solution(arr1, arr2):
    result = []
    counter = len(arr1) + len(arr2)
    common = list(set(arr1) - (set(arr1) - set(arr2)))
    
    if len(common) == 0:
        result.append('')
        return result
    if len(common) == 1:
        return common

    for elem in common:
        current = arr1.index(elem) + arr2.index(elem)
        if current < counter:
            result = []
            counter = current
            result.append(elem)

    return result
    
