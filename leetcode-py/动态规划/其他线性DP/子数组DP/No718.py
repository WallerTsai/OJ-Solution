from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max(map(max, dp)) # 这句话妙


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        ans = 0
        for i, x in enumerate(nums1):
            for j in range(n -1, -1, -1):
                y = nums2[j]
                if x == y:
                    dp[j + 1] = dp[j] + 1
                    ans = max(ans, dp[j + 1])
                else:
                    dp[j + 1] = 0
        return ans