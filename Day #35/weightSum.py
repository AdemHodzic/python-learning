
def solution(arr):
    return [sum([arr[i] for i in range(0, len(arr)) if i % 2 == 0]), sum([arr[i] for i in range(0, len(arr)) if not i % 2 == 0])]
