from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        i = 0
        while i < n:
            start = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:
                i += 1
            if i - start > 1:
                ans.append(f"{nums[start]}->{nums[i - 1]}")
            else:
                ans.append(str(nums[start]))
        return ans



