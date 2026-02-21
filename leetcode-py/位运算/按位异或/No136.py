from functools import reduce
from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums, 0)  # 8ms

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(int.__xor__, nums)    # 0ms

