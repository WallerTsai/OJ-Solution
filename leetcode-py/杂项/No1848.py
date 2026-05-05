from math import inf
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = inf  
        for i, x in enumerate(nums):
            if x == target:
                if abs(i - start) > ans:
                    break
                ans = min(ans, abs(i - start))
        return ans if ans != inf else -1




