from functools import cache
from typing import List


class Solution:
    @cache
    def find_max_factor(self,n: int) -> int:
        if n <= 2:
            return n
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return n // i
            i += 1
        return n
    
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        pre = 0
        for i in range(len(nums)-1):
            while nums[i] > nums[i+1]:
                stead =  self.find_max_factor(nums[i])
                if nums[i] == stead:
                    return -1
                else:
                    nums[i] //= stead
                    ans += 1
            if pre > nums[i]:
                return -1
            else:
                pre = nums[i]
        return ans  # 错误
    
class Solution:
    @cache
    def find_max_factor(self,n: int) -> int:
        if n <= 2:
            return n
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return n // i
            i += 1
        return n
    
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2, -1,-1):
            while nums[i] > nums[i+1]:
                stead =  self.find_max_factor(nums[i])
                if nums[i] == stead:
                    return -1
                else:
                    nums[i] //= stead
                    ans += 1
        return ans  # 131ms