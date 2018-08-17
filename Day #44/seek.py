def solution(string, indexes, sources, targets):
    to_replace = []

    for index, source, target in zip(indexes, sources, targets):
        if source in string and string.index(source) is index:
            to_replace.append((source, target))

    for element in to_replace:
        string = string.replace(element[0],element[1])

    return string
