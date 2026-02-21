from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3:
            if nums[-1] == nums[0] + nums[1]:
                return 3
            else:
                return 2
        ans = left = 0
        for right in range(2, n):
            if nums[right] != nums[right - 1] + nums[right - 2]:
                left = right - 1
            ans = max(ans, right - left + 1)
        return ans

fun = Solution()
fun.longestSubarray([1,2,1,1])
