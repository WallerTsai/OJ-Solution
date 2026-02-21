from typing import List
from functools import reduce
import math
import heapq

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        div = reduce(math.gcd,numsDivide)
        heapq.heapify(nums)

        ans = 0
        while nums:
            n = heapq.heappop(nums)
            if div % n == 0:
                return ans
            ans += 1
        
        return -1   # 67ms

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = math.gcd(*numsDivide)
        mn = min((x for x in nums if g % x == 0), default=0)
        return sum(x < mn for x in nums) if mn else -1

