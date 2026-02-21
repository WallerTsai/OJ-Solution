from typing import List


class Solution:
    # 定义状态, 状态转移
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * 7    # 空， 偶， 奇， 偶偶， 偶奇， 奇偶， 奇奇
        dp[0] = 1

        for num in nums:
            new_dp = dp[:]
            if num % 2 == 0:
                new_dp[1] = (new_dp[1] + dp[0]) % MOD
                new_dp[3] = (new_dp[3] + dp[1] + dp[5]) % MOD
                new_dp[5] = (new_dp[5] + dp[2] + dp[4] + dp[6]) % MOD
            else:
                new_dp[2] = (new_dp[2] + dp[0]) % MOD
                new_dp[4] = (new_dp[4] + dp[1] + dp[3] + dp[5]) % MOD
                new_dp[6] = (new_dp[6] + dp[2] + dp[4]) % MOD

            dp = new_dp

        return (sum(dp) - 1) % MOD