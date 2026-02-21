# 贪心4
# 难度：简单

import heapq
from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0  and k > 0:
                k -= 1
                nums[i] = -nums[i]
            else:
                break
        
        if k%2 == 1:
            min_index = nums.index(min(nums))
            nums[min_index] = -nums[min_index]

        return sum(nums)
    
class Solution:
    # 使用最小堆函数
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k and nums:
            if nums[0] < 0:
                heapq.heappush(nums,-heapq.heappop(nums))
                k -= 1
            else:
                if nums[0] and k % 2:
                    heapq.heappush(nums,-heapq.heappop(nums))
                break
        return sum(nums)