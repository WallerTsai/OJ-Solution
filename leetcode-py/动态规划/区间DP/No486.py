from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # dp[i][j]=max(nums[i]−dp[i+1][j],nums[j]−dp[i][j−1])
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = num

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        return dp[0][n -1] >= 0



