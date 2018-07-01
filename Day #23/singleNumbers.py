# Given an array of numbers nums, in which exactly two elements appear only once and all the other
# elements appear exactly twice. Find the two elements that appear only once.

# Input:  [1,2,1,3,2,5]
# Output: [3,5]

def solution(numbers):
    result = []

    for number in numbers:
        if not number in result:
            result.append(number)
        else:
            result.remove(number)

    return result
