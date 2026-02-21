from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        left = 0
        for right, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(right)

            if right < k - 1:
                continue
            
            while q[0] < left:
                q.popleft()

            ans.append(nums[q[0]])
            left += 1
        
        return ans  # 169ms