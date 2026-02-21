from bisect import bisect_left
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        def check(i:int) -> bool:
            count = 0
            for num in nums:
                count += (num - 1) // i + 1
            if count > n + maxOperations:
                return False
            return True
        left,right = 1,max(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left # 596ms
    
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        def check(i:int) -> bool:
            count = 0
            for num in nums:
                count += (num - 1) // i + 1
            if count > n + maxOperations:
                return False
            return True
        left,right = max(1,sum(nums)//(n+maxOperations)),sum(nums)//maxOperations
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left # 166ms
    
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        def check(i:int) -> bool:
            count = 0
            for num in nums:
                count += (num - 1) // i + 1
            if count > n + maxOperations:
                return False
            return True
        left = max(1,sum(nums)//(n+maxOperations))
        right = sum(nums)//maxOperations
        return bisect_left(range(left,right),True,key=check) + left # 151ms

