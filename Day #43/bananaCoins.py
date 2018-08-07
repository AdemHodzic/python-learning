def solution(coins, banana):
    coins = sorted(coins)
    counter = 0
    current = coins.pop()
    while banana > 0:
        if banana - current >= 0:
            banana -= current
            counter += 1
        else:
            current = coins.pop()
    return counter
