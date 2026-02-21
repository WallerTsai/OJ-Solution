from math import inf
from typing import List

# 数学题
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
    # 很容易发现，如果数组中有两个数相同，那么最小分数就一定是 0。
    # 修改最大的两个数为 nums[n−3]，最大得分为 nums[n−3]−nums[0]；
    # 修改最小的为 nums[1]，最大的为 nums[n−2]，最大得分为 nums[n−2]−nums[1]；
    # 修改最小的两个数为 nums[2]，最大得分为 nums[n−1]−nums[2]。
        min_num = min(nums[-3]-nums[0],nums[-2]-nums[1],nums[-1]-nums[2])
        return min_num

class Solution:
    # leetcode 最快
    # 时间复杂度为 O[n]
    def minimizeSum(self, nums: List[int]) -> int:
        min_vals = [inf] * 3
        max_vals = [-inf] * 3

        for num in nums:
            if num < min_vals[2]:
                if num < min_vals[1]:
                    if num < min_vals[0]:
                        min_vals = [num, min_vals[0], min_vals[1]]
                    else:
                        min_vals = [min_vals[0], num, min_vals[1]]
                else:
                    min_vals[2] = num

            if num > max_vals[2]:
                if num > max_vals[1]:
                    if num > max_vals[0]:
                        max_vals = [num, max_vals[0], max_vals[1]]
                    else:
                        max_vals = [max_vals[0], num, max_vals[1]]
                else:
                    max_vals[2] = num
        
        return min(max_vals[0] - min_vals[2], max_vals[1] - min_vals[1], max_vals[2] - min_vals[0])



