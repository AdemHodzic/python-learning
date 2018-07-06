# Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate 
# the number of 1's in their binary representation and return them as an array.

def solution(number):
    return map(lambda x: (bin(x)[2:]).count('1') ,range(0 , number + 1))
