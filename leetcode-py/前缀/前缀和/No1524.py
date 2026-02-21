from itertools import accumulate
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        odd = even = 0

        for x in accumulate(arr):
            if x % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return (ans + odd) % MOD    # 74ms


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd = sum(i & 1 for i in accumulate(arr))
        return odd * (len(arr) - odd + 1) % (10**9 + 7)
