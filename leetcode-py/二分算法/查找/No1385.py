from typing import List
from bisect import bisect_left
class Solution:
    # 暴力
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for i in arr1:

            flag = True

            for j in arr2:
                if abs(i-j) <= d:
                    flag = False
                    break

            if flag:
                res += 1

        return res  # 19ms
    
class Solution:
    # 排序+二分
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()

        for i in arr1:
            index = bisect_left(arr2,i-d)

            if i == len(arr2) or arr2[index] > i+d:
                res += 1
        
        return res  # 4ms