from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0
        for i, n in enumerate(nums):
            start = max(0,i - n)
            ans += sum(nums[start:i+1])
        return ans  # 12ms


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        li = [0]
        for i in range(len(nums)):
            li.append(nums[i] + li[-1])
        ans = 0
        for i,n in enumerate(nums):
            start = max(0,i - n)
            ans += li[i + 1] - li[start]
        return ans  # 3ms
    
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        for i, num in enumerate(nums):
            ans += s[i + 1] - s[max(i - num, 0)]
        return ans