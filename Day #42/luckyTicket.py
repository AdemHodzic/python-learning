def solution(ticket):
    ticket = str(ticket)
    half = len(ticket) / 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    return reduce(lambda x,y: x + int(y), first_half, 0) == reduce(lambda x,y: x + int(y), second_half, 0)
