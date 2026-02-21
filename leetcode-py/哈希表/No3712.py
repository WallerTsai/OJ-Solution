from collections import Counter
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for n, v in cnt.items():
            if v % k == 0:
                ans += n * v
        return ans
