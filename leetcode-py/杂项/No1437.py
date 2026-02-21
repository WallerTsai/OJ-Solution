from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        d = 0
        for num in nums:
            if num == 1:
                if d > 0:
                    return False
                d = k
            else:
                d -= 1
        return True




