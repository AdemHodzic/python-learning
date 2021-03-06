# In a given integer array nums, there is always exactly one largest element.  Find whether the largest 
# element in the array is at least twice as much as every other number in the array.  
# If it is, return the index of the largest element, otherwise return -1.

def solution(arr):
    temp = sorted(arr)
    biggest =  temp.pop()
    second =  temp.pop()
    if second * 2 == biggest:
        return arr.index(biggest)
    else:
        return -1
