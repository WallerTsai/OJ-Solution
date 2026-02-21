from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return 0
        nums.sort()
        res = 0
        for l in range(length-1,1,-1):
            l_edge = nums[l]
            left = 0
            right = l - 1
            while left < right:
                if nums[left] + nums[right] <= l_edge:
                    left += 1
                else:
                    res += right - left
                    # nums[left + 1] + nums[right]满足条件
                    # nums[left + 2] + nums[right]满足条件
                    # nums[right - 1] + nums[right]满足条件
                    ## 如果你考虑的是 # nums[left] + nums[right + n]满足条件
                    ## 这会导致重复
                    right -= 1
        return res  # 387ms