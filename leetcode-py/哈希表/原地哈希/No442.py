from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            y = abs(x) - 1
            if nums[y] < 0:
                ans.append(y + 1)
            nums[y] = -nums[y]
        return ans