from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        dp  = [[[1, 1] for _ in range(2)] for _ in range(n)]
        CAN_REM = INC = 1
        NOT_REM = DEC = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                dp[i][NOT_REM][DEC] = dp[i - 1][NOT_REM][INC] + 1
                dp[i][CAN_REM][DEC] = dp[i - 1][CAN_REM][INC] + 1 
            elif nums[i - 1] < nums[i]:
                dp[i][NOT_REM][INC] = dp[i - 1][NOT_REM][DEC] + 1
                dp[i][CAN_REM][INC] = dp[i - 1][CAN_REM][DEC] + 1 

            if i > 1 and nums[i - 2] != nums[i]:
                if nums[i - 2] < nums[i]:
                    dp[i][CAN_REM][INC] = max(dp[i][CAN_REM][INC], dp[i - 2][NOT_REM][DEC] + 1)
                else:
                    dp[i][CAN_REM][DEC] = max(dp[i][CAN_REM][DEC], dp[i - 2][NOT_REM][INC] + 1)

        return max(max(x[1]) for x in dp)