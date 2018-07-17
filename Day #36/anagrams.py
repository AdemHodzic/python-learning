def solution(full, sub):
    arr = []
    
    for i in range(0, len(full) - len(sub) + 1):
        temp = full[i:i+len(sub)]
        if sorted(temp) == sorted(sub):
            arr.append(i)
    return arr
