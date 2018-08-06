def solution(string):
    return False if len(string) % 2 == 1 else string[:len(string)/2] == string[len(string)/2:]
