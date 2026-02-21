from typing import List
from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        res = left = 0
        for right,num in enumerate(nums):
            if num == max_num:
                k -= 1
            while k <= 0:
                if nums[left] == max_num:
                    k += 1
                left += 1
            res += left
        return res  # 82ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        dq = deque()
        res = left = 0
        for right,num in enumerate(nums):
            if num == max_num:
                k -= 1
                dq.append(right)
            if k == 0:
                left = dq.popleft() + 1
                k += 1
            res += left
        return res  # 71ms
