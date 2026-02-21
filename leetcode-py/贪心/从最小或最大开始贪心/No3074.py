#贪心1
#难度：简单

from typing import List 

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        sum_num = sum(apple)
        res = 0
        while sum_num>0:
            sum_num -= capacity[res]
            res += 1

        return res
    

