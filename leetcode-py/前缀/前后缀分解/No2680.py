from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # suf[i] 表示 nums[i+1:] 的 OR
        suf = [0] * n
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] | nums[i+1]

        ans = pre = 0
        for x, s in zip(nums, suf):
            ans = max(ans, pre | (x << k) | s)
            pre |= x
        
        return ans