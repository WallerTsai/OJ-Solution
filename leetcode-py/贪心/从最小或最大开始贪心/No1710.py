# 难度简单
from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        res = 0
        for num, size in boxTypes:
            if num <= truckSize:
                res += num * size
                truckSize -= num
            else:
                res += truckSize * size
                break
        return res