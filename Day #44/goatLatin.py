def solution(sentence):
    vovels = ['a', 'e', 'i', 'o', 'u']

    sentence = sentence.split(' ')

    for index in range(len(sentence)):
        if sentence[index][0] in vovels:
            sentence[index] = sentence[index] + 'ma'
        else:
            first = sentence[index][0]
            sentence[index] = sentence[index][1:] + first + 'ma'

    sentence = list(map(lambda x: x + 'a' * (sentence.index(x) + 1), sentence))

    return ' '.join(sentence)
