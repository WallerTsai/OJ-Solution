from typing import List


class Solution:
    # 模拟
    def scoreDifference(self, nums: List[int]) -> int:
        r1 = r2 = 0
        changed = 0
        for i, num in enumerate(nums):
            if num % 2  == 1:
                r1, r2 = r2, r1
                changed += 1
            if (i + 1) % 6 == 0:
                r1, r2 = r2, r1
                changed += 1
            r1 += num
        return r1 - r2 if changed % 2 == 0 else r2 -r1



