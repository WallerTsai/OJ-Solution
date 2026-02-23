from functools import cache
from typing import List


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = float(k)
        @cache
        def dfs(i, t):
            if i == n:
                return 1 if abs(t - k) < 1e-9 else 0
            return dfs(i + 1, t) + dfs(i + 1, t * nums[i]) + dfs(i + 1, t / nums[i])
        ans = dfs(0, 1)
        dfs.cache_clear()
        return ans  # 671ms 这种不靠谱, 会出现精度损失

print(3 == 1 / 5 * 3 * 5)
print(1 / 5 * 3 * 5)


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = float(k)
        @cache
        def dfs(i, p, q):
            if i == n:
                return k == p / q 
            return dfs(i + 1, p * nums[i], q) + dfs(i + 1, p, q * nums[i]) + dfs(i + 1, p, q)
        ans = dfs(0, 1, 1)
        dfs.cache_clear()
        return ans