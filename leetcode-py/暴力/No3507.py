from math import inf
from typing import List


class Solution:
    # 暴力
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        flag = True
        while flag:
            pair = inf
            flag = False
            idx = -1

            if len(nums) == 1:
                break

            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    flag = True
                if nums[i] + nums[i + 1] < pair:
                    pair = nums[i] + nums[i + 1]
                    idx = i

            if flag:
                nums[idx] = pair
                nums.pop(idx + 1)
                count += 1

        return count
        






