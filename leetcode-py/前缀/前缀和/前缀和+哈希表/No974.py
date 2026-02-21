from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        pre_mod = 0
        cnt = defaultdict(int) 
        cnt[0] = 1

        for i, v in enumerate(nums):
            pre_mod = (pre_mod + v) % k
            ans += cnt[pre_mod]
            cnt[pre_mod] += 1

        return ans




