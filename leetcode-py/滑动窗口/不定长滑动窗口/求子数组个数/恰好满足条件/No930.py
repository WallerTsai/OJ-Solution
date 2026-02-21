from collections import Counter
from typing import List


class Solution:
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = left = 0
        temp = 0
        for right,num in  enumerate(nums):
            goal -= num
            if goal < 0:
                goal += 1
                temp = left
                left += 1
            if goal == 0:
                while left<=right and nums[left] != 1:
                    left += 1
                res += left - temp +1
        return res  # 错误

class Solution:
    # count(sum==k) = count(sum>=k+1) - count(sum>=k)
    # 元素和 ≥k 的子数组个数，减去元素和 ≥k+1 的子数组个数
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = l1 = l2 = temp_1 = temp_2 = 0
        for right,num in enumerate(nums):
            temp_1 += num
            temp_2 += num

            # 计算 sum >= k
            while l1 <= right and temp_1 >= goal:
                temp_1 -= nums[l1]
                l1 += 1

            # 计算 sum >= k + 1
            while l2 <= right and temp_2 >= goal+1:
                temp_2 -= nums[l2]
                l2 += 1
            
            res += l1-l2

        return res
    

class Solution:
    # 有点动态规划的味道
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = count = 0
        cnts = Counter({0:1})
        for num in nums:
            count += num
            res += cnts[count-goal]
            cnts[count] += 1
        return res

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = count = 0
        cnts = Counter({0:1})
        for num in nums:
            count += num
            if count >= goal:
                res += cnts[count-goal]
            cnts[count] += 1
        return res


