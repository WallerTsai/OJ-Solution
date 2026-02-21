from sortedcontainers import SortedDict,SortedList
from bisect import bisect_left

class MyCalendarTwo:
    # 暴力
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        # 先检查与重叠区有没有重复
        for s,e in self.overlaps:
            if startTime < e and s < endTime:
                return False
        
        # 再找有没有重叠部,添加到重叠区
        for s,e in self.calendar:
            if startTime < e and s < endTime:
                self.overlaps.append((max(startTime,s),min(endTime,e)))

        self.calendar.append((startTime,endTime))
        return True # 160ms
    

class MyCalendarTwo:
    # 使用有序字典(不行)
    def __init__(self):
        self.calendars = SortedDict()
        self.overlaps = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        # 先查找重叠区
        index = self.overlaps.bisect_left(endTime)
        if index != 0:
            if self.overlaps.values()[index-1] > startTime:
                return False
    # overlaps:
    # 10-23
    # 18-20
    # 查endTime = 22
    # 那么他会对比18-20，如果startTime = 21
    # 代码会返回ture，实际却是false
    # 键是有序的，而值不是有序的
            
        # # 再更新重叠区
        # index = self.calendars.bisect_left(endTime)
        # if index <= len(self.calendars) and index != 0:
        #     s,e = self.calendars.items()[index-1]
        #     if startTime < e:
        #         self.overlaps[max(startTime,s)] = min(endTime,e)
        # # 这里不能这样做因为startTime可能会和index前好几个发生重叠

        l_index = self.calendars.bisect_left(startTime)
        r_index = self.calendars.bisect_left(endTime)
        for i in range(max(0,l_index-1),r_index):
            s,e = self.calendars.items()[i]
            if startTime < e and s < endTime:
                self.overlaps[max(startTime,s)]=min(endTime,e)

        self.calendars[startTime] = endTime
        return True

 
class MyCalendarTwo:
    # 使用有序列表和有序字典
    # 有序字典不允许有同样的键
    def __init__(self):
        self.calendars = SortedDict()
        self.overlaps = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        # 先查找重叠区
        index = self.overlaps.bisect_left((endTime,0))
        if index > 0 and self.overlaps[index-1][1] > startTime:
                return False

        
        r_index = self.calendars.bisect_left(endTime)
        for i in range(0,r_index):
            s,e = self.calendars.items()[i]
            if startTime < e and s < endTime:
                self.overlaps.add((max(startTime,s),min(endTime,e)))

        temp = endTime
        if startTime in self.calendars:
            temp = max(self.calendars[startTime],temp)
        self.calendars[startTime] = temp
        return True # 1122ms
