from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(x != 1 for x in nums)
        if total == 0:
            return 0
        
        l = n   # 最快构造出 1 需要多少步
        for i in range(n):
            if nums[i] == 1:
                l = 0
                break
            for j in range(i - 1, -1, -1):
                if i - j >= l:
                    break
                g = gcd(nums[j], nums[i])
                if g == 1:
                    l = min(l, i - j)
                nums[j] = g
        
        if l == n:
            return -1
        if l == 0:
            return total
        return l + n - 1    # 4ms


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1
        
        l = n   # 最快构造出 1 需要多少步
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if i - j >= l:
                    break
                g = gcd(nums[j], nums[i])
                if g == 1:
                    l = min(l, i - j)
                nums[j] = g
        
        if l == n:
            return -1
        
        return l + n - 1    # 0ms
