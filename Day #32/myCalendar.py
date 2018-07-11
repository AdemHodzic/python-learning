class MyCalendar(object):

    def __init__(self):
        self.arr = []

    def book(self, start, end):
        
        temp = range(start, end)
         
        for num in temp[1:]:
            if num in  self.arr:
                return False

        self.arr.extend(temp)
        return True

