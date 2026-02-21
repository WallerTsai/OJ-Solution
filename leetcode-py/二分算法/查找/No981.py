from bisect import bisect_left, bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])
        # set 操作中的时间戳 timestamp 都是严格递增的
    def get(self, key: str, timestamp: int) -> str:
        index = bisect_right(self.map[key],timestamp,key=lambda x : x[0])
        if not index:
            return ""
        else:
            return self.map[key][index-1][1]    # 92ms

class TimeMap:

    def __init__(self):
        self.map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value
        # set 操作中的时间戳 timestamp 都是严格递增的
    def get(self, key: str, timestamp: int) -> str:
        keys = self.map[key].keys()
        index = bisect_right(keys,timestamp)
        if not index:
            return ""
        else:
            return self.map[key][keys[index-1]] # 851ms

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])
        # set 操作中的时间戳 timestamp 都是严格递增的
    def get(self, key: str, timestamp: int) -> str:
        if not self.map[key]:
            return ""
        if self.map[key][0][0] > timestamp:
            return ""
        index = bisect_right(self.map[key],timestamp,key=lambda x : x[0])
        
        return self.map[key][index-1][1]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)