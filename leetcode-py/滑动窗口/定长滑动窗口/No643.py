from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = cur_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if nums[i] > nums[i-k]:
                res = max(cur_sum,res)
        return res/k    #75ms
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        res = cur_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if nums[i] > nums[i-k]:
                res = max(cur_sum,res)
        return res/k    # 53ms
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        res = cur_sum = sum(nums[:k])
        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            if cur_sum > res:
                res = cur_sum
        return res/k    # 39ms