def solution(kids, cookies):

    kids = sorted(kids)
    counter = 0
    cookies = sum(cookies)
    
    for kid in kids:
        if cookies - kid >=0:
            cookies -= kid
            counter += 1
    return counter

