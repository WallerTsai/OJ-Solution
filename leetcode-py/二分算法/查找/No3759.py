from bisect import bisect_left
from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        i = 0
        n = len(nums)
        pre = -1
        while i < n:
            if nums[i] == pre:
                i += 1
                continue
            if k == 0:
                break

            k -= 1
            pre = nums[i]
            i += 1
                

        return n - i if k == 0 else 0   # 错误 题目要求的是"至少k个元素严格大于它"，不是"至少有k个不同的值大于它"
    

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        i = 0
        n = len(nums)
        pre = -1
        while i < n:
            if nums[i] == pre:
                i += 1
                k -= 1
                continue
            if k <= 0:
                break

            k -= 1
            pre = nums[i]
            i += 1
                

        return n - i if k <= 0 else 0   # 135ms
    
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if k == 0:
            return n
        
        target = nums[-k]
        ans = 0
        for num in nums:
            if num < target:
                ans += 1
            else:
                break
        return ans

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return n
        nums.sort()
        return bisect_left(nums, nums[-k])  # 小于第 k 大的元素个数