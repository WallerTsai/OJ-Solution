import heapq
from math import inf
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0
        min1 = nums[-1] - nums[3]
        min2 = nums[-2] - nums[2]
        min3 = nums[-3] - nums[1]
        min4 = nums[-4] - nums[0]

        res = min(min1,min2,min3,min4)
        return res  # 37ms
    
class Solution:
    # leetcode 最快
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return 0

        vmin, vmax = [], []
        for x in nums:
            # 4 smallest values
            if len(vmin) < 4:
                heapq.heappush(vmin, -x)
            else:
                if -vmin[0] > x:
                    heapq.heappop(vmin)
                    heapq.heappush(vmin, -x)
            # 4 largest values
            if len(vmax) < 4:
                heapq.heappush(vmax, x)
            else:
                if vmax[0] < x:
                    heapq.heappop(vmax)
                    heapq.heappush(vmax, x)
        
        vmin.sort()
        vmax.sort()

        ans = inf
        for i in range(4):
            ans = min(ans, vmax[i] + vmin[4 - i - 1])
        return ans  #15ms


