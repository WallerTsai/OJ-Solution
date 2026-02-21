from itertools import pairwise
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        pre = nums[0]
        for i in range(1, len(nums) - 1):
            cur = nums[i]
            nxt = nums[i + 1]
            if cur == nxt:
                continue
            if (cur > pre and cur > nxt) or (cur < pre and cur < nxt):
                ans += 1
            pre = cur
        return ans
    
class Solution:
    # 灵神
    # 状态机
    def countHillValley(self, nums: List[int]) -> int:
        ans = pre_state = 0
        for x, y in pairwise(nums):
            if x > y:
                if pre_state == -1:  # x 是峰
                    ans += 1
                pre_state = 1
            elif x < y:
                if pre_state == 1:  # x 是谷
                    ans += 1
                pre_state = -1
        return ans