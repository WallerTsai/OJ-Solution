from functools import cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)

        @cache
        def dfs(i:int, cur_sum = int) -> bool:
            if i == n:
                return cur_sum == s//2
            return dfs(i + 1,cur_sum + nums[i]) or dfs(i + 1, cur_sum)

        return s % 2 == 0 and dfs(len(nums) - 1, 0) # 2247ms

class Solution:
    # 递推
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2  # 注意这里把 s 减半了
        n = len(nums)
        f = [[False] * (s + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(nums):
            for j in range(s + 1):
                f[i + 1][j] = (j >= x and f[i][j - x]) or f[i][j]
        return f[n][s]  # 1118ms
    
class Solution:
    # 灵神
    # 空间压缩
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2  # 注意这里把 s 减半了
        f = [True] + [False] * s
        s2 = 0
        for i, x in enumerate(nums):
            s2 = min(s2 + x, s)
            for j in range(s2, x - 1, -1):
                f[j] = f[j] or f[j - x]
            if f[s]:
                return True
        return False