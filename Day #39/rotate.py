def solution(arr, number):
    return ((arr[::-1])[:number])[::-1] + arr[:len(arr) - number]
