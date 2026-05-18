from typing import List

class Solution:
    # 定义 dp[i][j] 为布尔值，表示：只考虑前 i 个奖励值，能否凑出总奖励恰好为 j 的状态。
    # dp[i][j] = dp[i-1][j - val]
    # dp[i][j] = dp[i-1][j] | dp[i-1][j - val]
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        n = len(nums)

        mx = nums[-1]
        dp = [[False] * (2 * mx) for _ in range(n + 1)]
        dp[0][0] = True

        for i, x in enumerate(nums):
            for j in range(2 * mx):
                # 不选
                dp[i + 1][j] = dp[i][j]
                # 选
                # dp限制：j >= x 目标和必须大于等于当前值
                # 题目限制：x 必须严格大于 之前的总和 x - j
                if j >= x and (j - x) < x:
                    dp[i + 1][j] = dp[i][j] | dp[i][j - x]
        
        for j in range(2 * mx - 1, -1, -1):
            if dp[n][j]:
                return j
            
        return 0


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        li = sorted(set(rewardValues))
        dp = {0}

        for v in li:
            nx_dp = { x + v for x in dp if x < v}
            dp |= nx_dp

        return max(dp)


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        li = sorted(set(rewardValues))
        dp = 1
        for v in li:
            mask = (1 << v) - 1
            valid = dp & mask
            dp |= (valid << v)
        return dp.bit_length() - 1