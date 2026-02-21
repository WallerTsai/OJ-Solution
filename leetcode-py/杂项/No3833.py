from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        total = sum(nums)
        for i, num in enumerate(nums):
            if i == n - 1:
                break
            total -= num
            avg = total // (n - i - 1)
            if num > avg:
                ans += 1
        return ans
    

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        suf_sum = ans = 0
        for i in range(n - 2, -1, -1):
            suf_sum += nums[i + 1]
            if nums[i] * (n - 1 - i) > suf_sum:
                ans += 1
        return ans