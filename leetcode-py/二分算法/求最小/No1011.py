from math import ceil
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low =  max(weights)
        hight = sum(weights)//days + 1
        while low < hight:
            mid = (low + hight) // 2
            count = 1
            temp = 0
            for i in weights:
                if temp + i <= mid:
                    temp += i
                else:
                    count += 1
                    temp = i
            if count <= days:
                hight = mid
            else:
                low = mid + 1
        return low  # 191ms

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        length = len(weights)
        maxw,minw = max(weights),min(weights)
        # 区间优化
        low = max(ceil(length/days) * minw,maxw)
        high = ceil(length/days) * maxw + 1

        while low < high:
            mid = (low + high) // 2
            count = 1
            temp = 0
            for i in weights:
                if temp + i <= mid:
                    temp += i
                else:
                    count += 1
                    temp = i
            if count > days:
                low = mid + 1
            else:
                high = mid

        return low  # 55ms