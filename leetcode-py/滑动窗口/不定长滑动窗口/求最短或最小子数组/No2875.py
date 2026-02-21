from math import inf
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = inf
        length = len(nums)
        sum_num = 0
        times = left = right = 0
        while left < length:
            if sum_num < target:
                sum_num += nums[right]
                right += 1
            if sum_num > target:
                sum_num -= nums[left]
                left += 1
            if sum_num == target:
                res = min(res,right + length * times - left)
                sum_num -= nums[left]
                left += 1
            if right == length:
                times += 1
                right = 0
        return res if res != inf else -1
    
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = inf
        length = len(nums)
        sum_num = 0
        times = left = right = 0
        while left < length:
            if right == length:
                times += 1
                right = 0
            if sum_num < target:
                sum_num += nums[right]
                right += 1
            elif sum_num == target:
                res = min(res,right + length * times - left)
                sum_num -= nums[left]
                left += 1
            else:
                sum_num -= nums[left]
                left += 1
        return res if res != inf else -1
    
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = inf
        length = len(nums)
        sum_num = 0
        times = left = right = 0
        while left < length:
            if sum_num == target:
                res = min(res,right + length * times - left)
                sum_num -= nums[left]
                left += 1
            if right == length:
                times += 1
                right = 0
            if sum_num < target:
                sum_num += nums[right]
                right += 1
            elif sum_num > target:
                sum_num -= nums[left]
                left += 1
        return res if res != inf else -1    # 超时 [1,1,1] 1_000_000_000
    
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        res = inf
        length = len(nums)
        sum_num = 0
        times = left = right = 0
        s = sum(nums)
        if s < target:
            times += target // s
            target = target % s
        while left < length:
            if sum_num == target:
                res = min(res,right + length * times - left)
                sum_num -= nums[left]
                left += 1
            if right == length:
                times += 1
                right = 0
            if sum_num < target:
                sum_num += nums[right]
                right += 1
            elif sum_num > target:
                sum_num -= nums[left]
                left += 1
        return res if res != inf else -1    # 47ms
    