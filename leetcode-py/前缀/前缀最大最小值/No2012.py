from typing import List

#前缀最大值 & 后缀最小值
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        # 后缀最小值
        bef_min = [0] * n
        bef_min[-1] = nums[-1]
        for i in range(n-2,1,-1):
            bef_min[i] = min(bef_min[i+1],nums[i])

        ans = 0
        pre_max = nums[0]
        for i in range(1,n-1):
            x = nums[i]
            if pre_max < x < bef_min[i+1]:
                ans += 2
            elif nums[i-1] < x < nums[i+1]:
                ans += 1
            pre_max = max(pre_max,x)

        return ans 