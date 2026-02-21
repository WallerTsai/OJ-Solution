from math import inf
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        pre = inf
        ans = 0
        for num in nums:
            ans = max(num - pre, ans)
            pre = min(pre, num)

        return ans if ans else -1

