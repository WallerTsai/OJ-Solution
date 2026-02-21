from math import isqrt
from typing import List
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        res = 0
        # 小妙
        for i,nums2 in enumerate(nums):
            if is_Prime(nums2[i]):
                res = max(res,nums2[i])
            if is_Prime(nums2[-1-i]):
                res = max(res,nums2[-1-i])
        return res  #85ms

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_Prime(num:int)->bool:
            if num < 2:
                return False
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return False
            return True
        res = 0
        for i,nums2 in enumerate(nums):
            # 如果比res小则退出判断
            if nums2[i]>res and is_Prime(nums2[i]):
                res = nums2[i]
            if nums2[-1-i]>res and is_Prime(nums2[-1-i]):
                res = nums2[-1-i]
        return res  #0ms
