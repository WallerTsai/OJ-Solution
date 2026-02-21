from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        ans = inf
        for i, num in enumerate(nums):
            cnt[num].append(i)
            if len(cnt[num]) >= 3:
                ans = min(ans,(cnt[num][-1] - cnt[num][-3]) * 2 )
        return ans if ans != inf else -1