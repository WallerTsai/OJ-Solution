from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt_n = 0
        for x in nums:
            x = abs(x)
            if (x > n or
                x == n and cnt_n > 1 or
                x < n and nums[x] < 0):
                return False
            if x == n:
                cnt_n += 1
            else:
                nums[x] = -nums[x]
        return True




