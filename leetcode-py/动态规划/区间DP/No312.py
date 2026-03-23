from typing import List

# 状态定义有点妙：dp[i][j] 为从区间[i, j] 选一个 k 下标的值 得到 val = nums[i] * nums[j] * nums[k]
# 这里 假设了 k 与i, j 相邻，那么他们上一个状态就是怎么得到 k 怎么和i, j 相邻 [i, k] 与 [k, j]
# 初始状态是 [i, i + 1, j], j = i + 2
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    val = nums[i] * nums[k] * nums[j]
                    val += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], val)
        
        return dp[0][n - 1]



