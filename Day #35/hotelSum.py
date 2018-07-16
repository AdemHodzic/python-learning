def solution(matrix):
    temp = []
    result = 0

    for arr in matrix:
        for i,x in enumerate(arr):
            if x == 0:
                temp.append(i)
            elif not i in temp:
                result += x
    return result
    
