from itertools import accumulate
from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        left_sum = 0
        right_sum = sum(nums)
        length = len(nums)
        for i,num in enumerate(nums):
            if i == length-1:
                break
            left_sum += num
            right_sum -= num
            if left_sum >= right_sum:
                res += 1
        return res # 60ms
    
class Solution:
    # 双和
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                res += 1
        return res # 47ms
    

class Solution:
    # 数学分析
    # l:左边和 s:总和
    # 题目要求 l >= s - l  ->  2*l >= s  ->  l > (s+1)//2
    # 利用accumulate()逐个求和
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        t = (sum(nums)+1) // 2
        for l in accumulate(nums[:-1]):
            if l >= t:
                res += 1
        return res # 35ms
    
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        t = (sum(nums) + 1) // 2
        return sum(s >= t for s in accumulate(nums[:-1]))
    
