from math import inf
from typing import List
class Solution:
    # 暴力
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = inf
        for left in range(len(nums)):
            value = 0
            for right in range(left,len(nums)):
                value |= nums[right]
                if value >= k:
                    res = min(res,right-left+1)
                    break
        return res if res != inf else -1    # 3ms

class Solution:
    # 灵感来自python方法accumulate()
    def bits_to_int(self,bits:Counter):
        res = 0
        for index,num in (bits.items()):
            if num > 0:
                res += 1 << index
        return res
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        bits = Counter()
        res = length + 1
        size = max(nums).bit_length()
        left = 0

        for right,num in enumerate(nums):
            # 添加到bits
            for i in range(size):
                bits[i] += (num >> i) & 1
            
            while left <= right and self.bits_to_int(bits) >= k:
                res = min(res,right-left+1)
                # 删除于bits
                for i in range(size):
                    bits[i] -= (nums[left] >> i) & 1
                left += 1

        return res if res != length+1 else -1
