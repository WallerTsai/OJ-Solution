from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for i in nums:
            ans += cnt[i]
            cnt[i] += 1
        return ans



