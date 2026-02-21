from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        MN, MX = min(nums), max(nums)
        aset = set(nums)
        ans = []
        for n in range(MN, MX + 1):
           if n not in aset:
               ans.append(n)

        return ans


