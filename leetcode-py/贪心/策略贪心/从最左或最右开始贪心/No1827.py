from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = pre = 0
        for n in nums:
            if n > pre:
                pre = n
            else:
                pre += 1
                ans += pre - n
        return ans


