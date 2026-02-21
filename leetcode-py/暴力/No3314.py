from typing import List

d = dict()
MX = 100_001
for i in range(MX):
    x = i | (i + 1)
    if x not in d:
        d[x] = i

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            if num in d:
                ans[i] = d[num]
        return ans