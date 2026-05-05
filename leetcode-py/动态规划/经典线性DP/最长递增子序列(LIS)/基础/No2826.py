from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        li = []
        ans = 0
        for x in nums:
            i = bisect_right(li, x)
            if i == len(li):
                li.append(x)
            else:
                ans += 1
                li[i] = x
        return ans

class Solution:
    # 灵神
    def minimumOperations(self, nums: List[int]) -> int:
        f = [0] * 4
        for x in nums:
            f[x] = max(f[1: x + 1]) + 1
        return len(nums) - max(f)


