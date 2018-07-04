# Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
# You may assume that each input would have exactly one solution, and you may not use the same element 

def solution(arr, target):
    result = []

    for number in arr:
        if target - number in arr:
            result.append(number)
            result.append(target - number)
            break
    
    final = []
    for num in result:
        final.append(arr.index(num))

    return sorted(final)
