from functools import cache
from math import inf
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dfs(i: int, t: int):
            if i == n:
                if t == target:
                    return 0
                return -inf
            # 优化一下
            if nums[i] > target - t:
                return dfs(i + 1, t)
            return max(dfs(i + 1, t), dfs(i + 1, t + nums[i]) + 1)
        
        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans if ans > 0 else -1   # 超时
    

class Solution:
    # 灵神
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0 if j == 0 else -inf
            if nums[i] > j:
                return dfs(i - 1, j)
            return max(dfs(i - 1, j), dfs(i - 1, j - nums[i]) + 1)

        ans = dfs(len(nums) - 1, target)
        dfs.cache_clear()  # 防止爆内存
        return ans if ans > 0 else -1



class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-inf] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(target + 1):
                if j < x:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - x] + 1)
        return dp[n][target] if dp[n][target] > 0 else -1