def solution(number):
    counter = 0
    for i in range(0, number):
        if not i == switch(i):
            counter += 1
    return counter

def switch(number):
    if number == 2:
        return 5
    elif number == 5:
        return 2
    elif number == 6:
        return 9
    elif number == 9:
        return 6
    else:
        return number
