from collections import defaultdict
from math import inf
from typing import List

fmin = lambda x, y : x if x < y else y
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        ans = inf
        cnt = defaultdict(int)
        for i, num in enumerate(nums):
            if num in cnt:
                ans = fmin(ans,i - cnt[num])
            cnt[int(str(num)[::-1])] = i
        return ans if ans != inf else - 1

