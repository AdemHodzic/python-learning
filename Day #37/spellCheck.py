def solution(string):
    if len(string) < 3:
        return True
    elif len(string) == 3 and string[0:2] == 'ei':
        return string[-1] == 'c'
    elif len(string) == 3 and string[0:2] == 'ie':
        return not string[-1] == 'c'
    else:
        string = string[::-1]
        for i in range(2, len(string)):
            temp = string[i-2:i+1]
            if 'ei' == temp[0:2] and  temp[-1] == 'c':
                return False
            if 'ie' == temp[0:2] and not temp[-1] == 'c':
                return False
        return True
