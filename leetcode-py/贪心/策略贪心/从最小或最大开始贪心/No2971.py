from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_P = -1
        cur_P = 0

        left_p = 0
        for right_p in range(len(nums)):
            cur_P += nums[right_p]
            if right_p - left_p < 2:
                continue
            
            if nums[left_p] < cur_P - nums[left_p]:
                max_P = max(cur_P,max_P)
            else:
                cur_P -= nums[left_p]
                left_p += 1
        return max_P
    ### 逻辑错误

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(0,len(nums)-2):
            if nums[i] >= sum(nums[i+1:]):
                continue
            else:
                return nums[i] + sum(nums[i+1:])
        return -1   # 87ms
            
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        cur_sum = sum(nums)
        for i in range(0,len(nums)-2):

            if 2*nums[i] >= cur_sum:
                cur_sum -= nums[i]
                continue
            else:
                return cur_sum
        return -1   # 78ms




fun = Solution()
outcome = fun.largestPerimeter([1,12,1,2,5,50,3])
print(outcome)





