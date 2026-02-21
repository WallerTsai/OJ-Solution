from collections import defaultdict
from typing import List
import heapq

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = 0
        dd = defaultdict(int)
        for right,num in enumerate(nums):
            dd[num] += 1
            cnt = max(dd.values())
            if cnt > k:
                dd[nums[left]] -= 1
                left += 1
        return right - left + 1 # 超时
    
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        dd = defaultdict(int)
        for right,num in enumerate(nums):
            dd[num] += 1
            while dd[num] > k:
                dd[nums[left]] -= 1
                left += 1
            res = max(res,right-left+1)
        return res  # 330ms




