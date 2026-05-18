from functools import cache
from math import inf
from typing import List

fmax = lambda x, y : x if x > y else y
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache      
        def dfs(i: int, j: int):
            if i < 0 or j < 0:
                return -inf
            
            res1 = nums1[i] * nums2[j] + fmax(dfs(i - 1, j - 1), 0)
            res2 = dfs(i - 1, j)
            res3 = dfs(i, j - 1)

            return max(res1, res2, res3)

        ans = dfs(len(nums1) - 1, len(nums2) - 1)
        dfs.cache_clear()
        return ans  # 458ms
    

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        f = [[-inf] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                f[i + 1][j + 1] = max(max(f[i][j], 0) + x * y, f[i][j + 1], f[i + 1][j])
        return f[n][m]
    
    