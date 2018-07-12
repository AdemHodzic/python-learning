def solution(arr):

    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    obj = dict()

    for a,m in zip(alpha, morse):
        obj.update({a:m})

    result = []

    for word in arr:
        temp = ''
        for char in word:
            temp += obj[char]
        result.append(temp)

    return len(list(set(result)))
