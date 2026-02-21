from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:
        a1 = a2 = 0

        for x in nums:
            a1,a2 = a2,max(a1 + x,a2)

        return a2
    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.rob1(nums[2:-1]),self.rob1(nums[1:]))



