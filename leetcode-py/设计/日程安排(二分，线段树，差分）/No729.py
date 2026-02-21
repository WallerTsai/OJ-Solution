from sortedcontainers import SortedDict
from bisect import bisect_right
class MyCalendar:
    # 直接
    def __init__(self):
        self.calendars = set()

    def book(self, startTime: int, endTime: int) -> bool:
        flag = True
        for i in self.calendars:
            if startTime >= i[1] or endTime <= i[0]:
                continue
            else:
                flag = False
                break
        
        if flag:
            self.calendars.add((startTime,endTime))
        return flag # 278ms
    

class MyCalendar:
    # 使用有序字典(这个包需要额外导入，可能比赛时候不给用)
    def __init__(self):
        self.calendars = SortedDict()


    def book(self, startTime: int, endTime: int) -> bool:
        index = self.calendars.bisect_left(endTime)
        if index <= len(self.calendars) and index != 0:
            if self.calendars.values()[index-1] > startTime:
                return False
        
        self.calendars[startTime] = endTime
        return True # 64ms

class MyCalendar:
    # 手动维护+二分
    def __init__(self):
        self.calendars = []

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0
        right = len(self.calendars)-1
        while left <= right:
            mid = (left + right) // 2
            s,e = self.calendars[mid]
            if endTime <= s:
                right = mid -1
            elif startTime >= e:
                left = mid + 1
            else:
                return False
        self.calendars.insert(left,(startTime,endTime))
        return True # 36ms