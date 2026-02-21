from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        aset = set(nums)
        MAX = max(nums)
        i = k
        while i <= MAX:
            if i not in aset:
                return i
            i += k
        return i
    
fun = Solution()
fun.missingMultiple([8,2,3,4,6], 2)