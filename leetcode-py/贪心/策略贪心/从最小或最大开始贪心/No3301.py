# 难度中等
from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        res = 0
        temp = maximumHeight[0]+1
        for i in maximumHeight:
            if i < temp:
                temp = i
            else:
                temp -= 1

            if temp == 0:
                return -1
            
            res += temp
        return res  # 195ms
    
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        res = 0
        temp = maximumHeight[0]+1
        for i in maximumHeight:
            if i < temp:
                temp = i
            else:
                temp -= 1

                if temp == 0:   # 这种情况只能在i==temp出现
                    return -1
            
            res += temp
        return res  # 175ms
