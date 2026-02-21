from collections import defaultdict
from typing import List
from bisect import bisect_left,bisect_right


class RangeFreqQuery:
    # 暴力，模拟
    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, value: int) -> int:
        res = 0
        for i in self.arr[left:right+1]:
            if i == value:
                res += 1
        return res  # 超时
    
# 这方法没想到
class RangeFreqQuery:
    # 统计每个元素的下标
    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for index,value in enumerate(arr):
            pos[value].append(index)
        self.pos = pos

    def query(self, left: int, right: int, value: int) -> int:
        arr = self.pos[value]
        L = bisect_left(arr,left)
        R = bisect_right(arr,right)
        return R-L


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)