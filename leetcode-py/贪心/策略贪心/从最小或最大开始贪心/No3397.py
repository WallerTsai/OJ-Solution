from math import inf
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        pre = -inf    #记录上一个数的大小
        for num in nums:
            left = max(num-k,pre+1) #左区间
            if left <= num+k:   #左区间有效
                res += 1
                pre = left
            else:               #无效
                pre = num+k
        return res




