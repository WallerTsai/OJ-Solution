from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = -inf
        left = f = 0
        l = r = 0
        for i, x in enumerate(arr):
            if f + x >= x:
                f += x
            else:
                f = x
                left = i
            if f > ans:
                ans = f
                l = left
                r = i
        
        y = min(arr[l: r + 1])
        if l != r and y < 0:
            ans -= y
        return ans  # 错误
    

class Solution:
    # dp
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = arr[0]
        dp[0][1] = -inf

        ans = arr[0]
        for i in range(1, n):
            # 不删除
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            # 删除
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])

            ans = max(ans, dp[i][0], dp[i][1])

        return ans


class Solution:
    # 前后缀分解
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        left = [0] * n
        s = 0
        for i in range(n):
            s = max(s + arr[i], arr[i])
            left[i] = s

        right = [0] * n
        s = 0
        for i in range(n - 1, -1, -1):
            s = max(s + arr[i], arr[i])
            right[i] = s

        ans = arr[0]
        for i in range(1, n - 1):
            ans = max(ans, left[i], left[i - 1] + right[i + 1])
        ans = max(ans, left[-1])
    
        return ans