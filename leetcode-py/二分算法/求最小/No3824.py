from bisect import bisect_left
from math import cbrt, ceil, isqrt, sqrt
from typing import List

print(isqrt(7))

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        MX = max(nums)
        x = isqrt(MX)
        return x if pow(x, 2) == MX else x + 1  # 错误
    

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def check(k):
            res = 0
            for num in nums:
                res += ceil(num / k)
            return res <= pow(k, 2)
        lo = 1
        hi = max(max(nums), len(nums))
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    

class Solution:
    # 灵神
    def minimumK(self, nums: List[int]) -> int:
        n = len(nums)

        def check(k: int) -> bool:
            return n + sum((x - 1) // k for x in nums) <= k * k

        left = ceil(sqrt(n))  # 答案的下界
        right = max(nums)
        return bisect_left(range(right), True, left, key=check)
    

class Solution:
    # leetcode 大佬
    def minimumK(self, nums: List[int]) -> int:
        n = len(nums)
        nonPositive = lambda nums, k: sum((x - 1) // k for x in nums) + n
        # 假设low、high分别是答案(ans)的下界和上界
        # 由题目知：
        # nonPositive(nums, ans) <= ans * ans
        # nonPositive(nums, ans - 1) > (ans - 1) * (ans - 1)
        # 由nonPositive的单调性可得：
        # nonPositive(nums, low - 1) >= nonPositive(nums, ans - 1) > (ans - 1) * (ans - 1)
        # nonPositive(nums, high) <= nonPositive(nums, ans) <= ans * ans
        low = max(ceil(sqrt(n)), ceil(cbrt(sum(nums)))) # 这个值已较接近答案
        high = isqrt(nonPositive(nums, low)) + 1
        while low < high:
            k = low + high >> 1
            t = nonPositive(nums, k)
            if t <= k * k:
                high = k
                # ans >= isqrt(nonPositive(nums, high))
                low = max(low, isqrt(t))
            else:
                low = k + 1
                # ans <= isqrt(nonPositive(nums, low - 1)) + 1
                high = min(high, isqrt(t) + 1)
        return low