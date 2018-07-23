def solution(string, arr):
    counter = 0

    for word in arr:
        uni = set(word)
        for i,w in enumerate(list(uni)):
            if word.count(w) > string.count(w):
                break
            if i == len(uni) - 1:
                counter += 1
    return counter
