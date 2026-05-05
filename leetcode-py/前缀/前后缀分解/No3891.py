from functools import cache
from math import inf
from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        def func(i, n):
            res = 0
            while i < n - 1:
                if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
                    res += max(nums[i - 1], nums[i + 1]) - nums[i] + 1
                i += 2
            return res
        
        ans = 0
        n = len(nums)
        if n & 1:
             ans = func(1, n)
        else:
            ans = min(func(1, n), func(2, n))
        
        return ans  # 错误


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n & 1:
            i = 1
            ans = 0
            while i < n - 1:
                if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
                    ans += max(nums[i - 1], nums[i + 1]) - nums[i] + 1
                i += 2
            return ans

        target = n // 2 - 1
        @cache
        def dfs(i, count):
            if i >= n - 1:
                return 0 if count == target else inf
            res = 0
            if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
                res += max(nums[i - 1], nums[i + 1]) - nums[i] + 1
            res += min(dfs(i + 2, count + 1), dfs(i + 3, count + 1))
            return res
        
        ans = min(dfs(1, 0), dfs(2, 0))
        dfs.cache_clear()
        return ans  # 超时


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        if n & 1:
            i = 1
            ans = 0
            while i < n - 1:
                if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
                    ans += max(nums[i - 1], nums[i + 1]) - nums[i] + 1
                i += 2
            return ans

        @cache
        def dfs(i, flag):
            if i >= n - 1:
                return 0 
            res = 0
            if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
                res += max(nums[i - 1], nums[i + 1]) - nums[i] + 1
            if not flag or i + 3 >= n - 1:
                res += dfs(i + 2, flag)
            else:
                res += min(dfs(i + 2, flag), dfs(i + 3, flag = False))
            return res
        
        ans = min(dfs(1, True), dfs(2, True))
        dfs.cache_clear()
        return ans
    

class Solution:
    # 灵神
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 2, 0, -2):
            suf[i] = suf[i + 2] + max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)

        if n % 2 > 0:
            # 修改所有奇数下标
            return suf[1]

        ans = suf[2]  # 修改 [2,n-2] 中的所有偶数下标
        pre = 0
        # 枚举修改 [1,i] 中的奇数下标，以及 [i+3,n-2] 中的偶数下标
        for i in range(1, n - 1, 2):
            pre += max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)
            ans = min(ans, pre + suf[i + 3])

        return ans

