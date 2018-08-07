import string

def solution(letters):
    all_letters = list(string.ascii_lowercase)
    min = all_letters.index(letters[0])
    max = all_letters.index(letters[-1]) + 1
    sliced = all_letters[min:max]
    result = list(set(sliced) - set(letters))
    return result.pop() if len(result) == 1 else ''
