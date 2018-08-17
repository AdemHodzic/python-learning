def solution(image):
    for i in range(len(image)):
        image[i] = (image[i])[::-1]
        image[i] = list(map(lambda x: 1 if x == 0 else 0, image[i]))

    return image
