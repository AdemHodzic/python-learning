from math import floor

class MedianFinder(object):

    def __init__(self):
        self.arr = []

    def addNum(self, num):
        self.arr.append(num)

    def findMedian(self):
        if len(self.arr) % 2 == 0:
            index = int(len(self.arr) / 2) 
            print('soludiotn is  ',)
            return (self.arr[index] + self.arr[index - 1]) / float(2)
        else:
            index = int(floor(len(self.arr) / 2))
            return self.arr[index]
