from functools import cache
from math import inf
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)

        @cache
        def dfs(i, j, k):
            if i < k - 1 or j < k - 1:
                return -inf
            
            if k == 0:
                return 0
            
            # 选
            res = dfs(i - 1, j - 1, k - 1) + nums1[i] * nums2[j]

            # 不选
            res = max(res, dfs(i - 1, j, k), dfs(i, j - 1, k))

            return res

        ans = dfs(n - 1, m - 1, k)
        dfs.cache_clear()
        return ans


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], K: int) -> int:
        n, m = len(nums1), len(nums2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for k in range(1, K + 1):
            nf = [[-inf] * (m + 1) for _ in range(n + 1)]
            for i in range(k - 1, n - (K - k)):  # 后面还要选 K-k 个下标对
                for j in range(k - 1, m - (K - k)):
                    nf[i + 1][j + 1] = max(nf[i][j + 1], nf[i + 1][j], f[i][j] + nums1[i] * nums2[j])
            f = nf
        return f[n][m]
