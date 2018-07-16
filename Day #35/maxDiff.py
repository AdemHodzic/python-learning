def solution(arr):
    return max([abs(arr[i] - arr[i+1]) for i in range(len(arr) - 1)])
