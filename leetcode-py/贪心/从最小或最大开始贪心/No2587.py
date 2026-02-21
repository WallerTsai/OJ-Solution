# 难度中等
import bisect
from itertools import accumulate
from typing import List
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        nums.sort()
        index = bisect.bisect_right(nums,0)
        if index == 0:
            return len(nums)
        elif index == len(nums):
            return 0
        else:
            res += len(nums) - index
            cur_sum += sum(nums[index:])

        for i in range(index-1,-1,-1):
            cur_sum += nums[i]
            if cur_sum <= 0:
                break
            else:
                res += 1
        return res  # 91ms

class Solution:
    # 艾哥代码
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(s > 0 for s in accumulate(nums)) # 105ms

fun = Solution()
fun.maxScore([2,-1,0,1,-3,3,-3])