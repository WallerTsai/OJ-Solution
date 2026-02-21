from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for left, num in enumerate(nums):
            if num == 0:
                right = left
                while right < n and nums[right] == 0:
                    ans += right - left + 1
                    right += 1
        return ans # 致命错误
    
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = left = 0
        n = len(nums)
        while left < n:
            if nums[left] == 0:
                right = left
                while right < n and nums[right] == 0:
                    print(left, right)
                    ans += right - left + 1
                    right += 1
                left = right
            left += 1
        return ans  # 367ms
    
class Solution:
    # 增量思想
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
                ans += zero_cnt
            else:
                zero_cnt = 0
        return ans  # 31ms
    
class Solution:
    # 滑动窗口思想
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        last = -1
        for i, x in enumerate(nums):
            if x:
                last = i  # 记录上一个非 0 元素的位置
            else:
                ans += i - last
        return ans