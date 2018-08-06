def solution(sequence, timers):
    obj = {}
    for i in range(len(timers)):
        key = sequence[i]
        value = timers[i]
        if key not in obj.keys():
            obj[key] = [value]
        else:
            obj[key].append(value)

    return check(obj)

def check(obj):
    for key in obj:
        if not obj[key] == sorted(obj[key]):
            return False
    return True
