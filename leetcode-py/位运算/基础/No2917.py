from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(max(nums).bit_length()):
            cnt = sum(x >> i & 1 for x in nums)
            if cnt >= k:
                res |= 1<<i # 并
        return res

