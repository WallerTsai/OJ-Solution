from collections import Counter
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
        return res if res != inf else -1    # 超时
    
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

        left = 0

        for right,num in enumerate(nums):
            # 添加到bits
            for i in range(32):
                bits[i] += (num >> i) & 1
            
            while left <= right and self.bits_to_int(bits) >= k:
                res = min(res,right-left+1)
                # 删除于bits
                for i in range(32):
                    bits[i] -= (nums[left] >> i) & 1
                left += 1

        return res if res != length+1 else -1   # 4804 ms

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

        return res if res != length+1 else -1   # 2324ms
    
class Solution:
    # leetcode 官方
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 30
        res = inf
        def calc(bits):
            return sum(1 << i for i in range(30) if bits[i] > 0)

        left = 0
        for right in range(n):
            for i in range(30):
                bits[i] += (nums[right] >> i) & 1
            while left <= right and calc(bits) >= k:
                res = min(res, right - left + 1)
                for i in range(30):
                    bits[i] -= (nums[left] >> i) & 1
                left += 1

        return -1 if res == inf else res

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            if x >= k:
                return 1
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                if nums[j] >= k:
                    ans = min(ans, i - j + 1)
                j -= 1
        return ans if ans < inf else -1
