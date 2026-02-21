from math import inf
from typing import List


class Solution:
    # 看似组合题目,实际上是排序区间题目
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = inf
        for i in range(k,len(nums)+1):
            res = min(res,nums[i-1]-nums[i-k])
        
        return res  # 4ms

