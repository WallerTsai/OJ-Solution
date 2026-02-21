from bisect import bisect_left
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap_id = 0
        # 记录每个下标的修改历史记录
        self.cache = defaultdict(list)
        

    def set(self, index: int, val: int) -> None:
        self.cache[index].append((self.cur_snap_id,val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 注意 这里 snap_id 有诈
        i = bisect_left(self.cache[index],snap_id+1,key= lambda x:x[0])
        if i == 0:
            return 0
        else:
            return self.cache[index][i-1][1]