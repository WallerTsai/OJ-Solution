from bisect import bisect_left, bisect_right
from collections import Counter
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)//2
        res = len(nums)
        while left < len(nums)//2 and right < len(nums):
            if nums[left] < nums[right]:
                res -= 2
                left += 1
                right += 1
            else:
                right += 1
        return res  # 59ms

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)//2
        res = len(nums)
        while left < len(nums)//2 and right < len(nums):
            if nums[left] < nums[right]:
                res -= 2
                left += 1
                right += 1
            else:
                right += 1
        return res
    
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        def merge(nums:List[int]) -> List[int]:
            length = len(nums)
            if length < 2:
                return nums
            mid = length//2
            L = merge(nums[:mid])
            R = merge(nums[mid:])
            left = right = 0
            while left < len(L) and right < len(R):
                if L[left] < R[right]:
                    L.pop(left)
                    R.pop(right)
                else:
                    right += 1
            return L + R 
        return len(merge(nums)) # 错误 [2,3,4,4,4]

class Solution:
    # 羊神
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        v = max(Counter(nums).values())
        return n % 2 if v * 2 <= n else n - (n - v) * 2 # 55ms
    
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        v = Counter(nums).most_common(1)[0][1]
        return n % 2 if v * 2 <= n else n - (n - v) * 2 # 52ms

class Solution:
    # 灵神
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums[n // 2]
        # 下面还是统计某个元素最大出现次数
        max_cnt = bisect_right(nums, x) - bisect_left(nums, x)
        return max(max_cnt * 2 - n, n % 2)  # 0ms



