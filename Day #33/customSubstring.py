def solution(string, substring):

    for index,char in enumerate(string):
        if char == substring[0] and contains(string[index:index + len(substring)], substring):
            return index
    return -1

def contains(string, sub):
    return string == sub
