from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        pre_sum = 1
        for i in range(n):
            cur_sum = pre_sum
            for j in range(i+1,n):
                cur_sum *= nums[j]
            ans.append(cur_sum)
            pre_sum *= nums[i]
        return ans  # 超时

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_sum = nums[:]
        right_sum = nums[:]
        for i in range(1,n):
            left_sum[i] = nums[i] * left_sum[i-1]
        for j in range(n-2,-1,-1):
            right_sum[j] = nums[j] * right_sum[j+1]

        nums[0] = right_sum[1]
        nums[-1] = left_sum[-2]
        for k in range(1,n-1):
            nums[k] = left_sum[k-1] * right_sum[k+1]
        
        return nums # 28ms
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf  # O(1) 空间复杂度