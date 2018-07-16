from collections import deque, Counter

def solution(string):

    cnt = Counter(string)
    sides = []
    center = deque()

    for letter, number in cnt.items():
        occur, mod = divmod(number, 2)
        if not mod:
            sides.append(letter * occur)
            continue
        if not len(center) == 0:
            return False
        center.append(letter * number)
    center.extendleft(sides)
    center.extend(sides)
    palindrome = ''.join(center)
    return sorted(palindrome) == sorted(string)
