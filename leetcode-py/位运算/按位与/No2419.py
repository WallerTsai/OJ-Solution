from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 1
        MX = nums[0]
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > MX:
                MX = nums[i]
                ans = length = 1
            elif nums[i] == MX:
                length += 1
                ans = max(length, ans)
            else:
                length = 0
        return ans



