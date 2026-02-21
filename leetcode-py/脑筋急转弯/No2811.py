from functools import cache
from itertools import pairwise
from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        def backtrace(i: int):
            if i == n - 2:
                return sum(nums[i:]) >= m
            elif i == n - 1:
                return True
            if sum(nums[i:i + 2]) >= m and backtrace(i + 2):
                return True
            if backtrace(i + 1) and sum(nums[i + 1:]) >= m:
                return True
            return False
        return backtrace(0) # 错误

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        pre_sum  = [0] + nums
        for i in range(1,n + 1):
            pre_sum[i] += pre_sum[i - 1]
        print(pre_sum)
        @cache
        def dfs(l: int, r: int):
            if r - l <= 1:
                return True
            
            for i in range(l + 1, r + 1):
                if i - l == 1 and pre_sum[r + 1] - pre_sum[i] >= m:
                    if dfs(i, r):
                        return True

                if r - i == 0 and pre_sum[i] - pre_sum[l] >= m:
                    if dfs(l,i - 1):
                        return True

                if pre_sum[i] - pre_sum[l] >= m and pre_sum[r + 1] - pre_sum[i] >= m:
                    if dfs(l, i - 1) and dfs(i, r):
                        return True
                
            return False

        return dfs(0, n - 1)    # 1609ms
    
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        return len(nums) <= 2 or any(x + y >= m for x, y in pairwise(nums)) # 0ms
    
fun = Solution()
fun.canSplitArray([2, 3, 3, 2, 3], 6)