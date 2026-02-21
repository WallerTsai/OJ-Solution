from math import inf
from sortedcontainers import SortedDict as SD
from sortedcontainers import SortedList
from bisect import bisect_left,bisect_right

class MyCalendarThree:
    # 差分
    # 来自leetcode大佬
    def __init__(self):
        self.f = SD()       #差分

    def book(self, start: int, end: int) -> int:
        if start not in self.f:
            self.f[start] = 0
        self.f[start] += 1

        if end not in self.f:
            self.f[end] = 0
        self.f[end] -= 1

        res = 0
        acc = 0             #差分，回收
        for i, diff in self.f.items():
            acc += diff
            res = max(res, acc)
        return res  # 1368ms
    
class MyCalendarThree:
    # leetcode最快
    # 太强了
    def __init__(self):
        self.max_value = 0
        self.record = [[-inf,0],[inf,0]]

    def book(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.record,startTime,key=lambda x:x[0])
        if not self.record[l][0] == startTime:
            self.record.insert(l,[startTime,self.record[l-1][1]])
        r = bisect_left(self.record,endTime,key=lambda x:x[0])
        if not self.record[r][0] == endTime:
            self.record.insert(r,[endTime,self.record[r-1][1]])
        for i in range(l,r):
            self.record[i][1] += 1
            self.max_value = max(self.max_value,self.record[i][1])
        return self.max_value   # 51ms
    
class MyCalendarThree:
    # leetcode 第二快
    def __init__(self) -> None:
        self.calendars = [0,inf]
        self.cnt = [0,0]

    def book(self, startTime: int, endTime: int) -> int:
        l = bisect_right(self.calendars,startTime)
        r = bisect_left(self.calendars,endTime)

        if endTime < self.calendars[r]:
            self.calendars.insert(r,endTime)
            self.cnt.insert(r,self.cnt[r-1])

        for i in range(l,r):
            self.cnt[i] += 1

        if startTime == self.calendars[l-1]:
            self.cnt[l-1] += 1
        else:
            self.calendars.insert(l,startTime)
            self.cnt.insert(l,self.cnt[l-1]+1)
        
        return max(self.cnt)    # 77ms

class MyCalendarThree:
    # leetcode 第二快（改）
    def __init__(self) -> None:
        self.calendars = [0,inf]
        self.cnt = [0,0]

    def book(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.calendars,startTime)
        r = bisect_left(self.calendars,endTime)

        if endTime < self.calendars[r]:
            self.calendars.insert(r,endTime)
            self.cnt.insert(r,self.cnt[r-1])

        for i in range(l,r):
            self.cnt[i] += 1

        if startTime != self.calendars[l]:
            self.calendars.insert(l,startTime)
            self.cnt.insert(l,self.cnt[l-1]+1)
        
        return max(self.cnt)    # 74ms

class MyCalendarThree:

    def __init__(self):
        self.calendars = SortedList([0,inf])
        self.cnt = [0,0]


    def book(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.calendars,startTime)
        r = bisect_left(self.calendars,endTime)

        if endTime < self.calendars[r]:
            self.calendars.add(endTime)
            self.cnt.insert(r,self.cnt[r-1])

        for i in range(l,r):
            self.cnt[i] += 1

        if startTime != self.calendars[l]:
            self.calendars.add(startTime)
            self.cnt.insert(l,self.cnt[l-1]+1)

        return max(self.cnt)    # 164ms

class MyCalendarThree:
    # 使用有序列表
    def __init__(self):
        self.calendars = SortedList([0,inf])
        self.cnt = [0,0]
        self.max_value = 0


    def book(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.calendars,startTime)

        if startTime != self.calendars[l]:
            self.calendars.add(startTime)
            self.cnt.insert(l,self.cnt[l-1])

        r = bisect_left(self.calendars,endTime)

        if endTime < self.calendars[r]:
            self.calendars.add(endTime)
            self.cnt.insert(r,self.cnt[r-1])

        for i in range(l,r):
            self.cnt[i] += 1
            self.max_value = max(self.max_value,self.cnt[i])

        return self.max_value   # 107ms