from itertools import accumulate
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        count = 0
        res = 0
        for right,num in enumerate(nums):
            count += num
            while count*(right-left+1) >= k:
                count -= nums[left]
                left += 1
            res += right - left + 1
        return res  # 128ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = cur_sum = ans = 0
        for right, num in enumerate(nums):
            cur_sum += num
            while cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1
            ans += right - left + 1
        return ans

class Solution:
    # 前缀和 + 二分
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(1, len(s)):
            l, r = 0, i
            while l < r:
                mid = (l + r + 1) >> 1
                if (s[i] - s[i - mid]) * mid < k:
                    l = mid
                else:
                    r = mid - 1
            ans += l
        return ans
    
class Solution:
    # 滑动窗口 + 前缀和
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        left = ans = 0
        for right, num in enumerate(nums):
            while (s[right+1] - s[left]) * (right - left + 1) >= k:
                left += 1
            ans += right - left + 1
        return ans