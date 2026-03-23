from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        ans = left = 0

        for right, x in enumerate(nums):
            while min_dq and x <= nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(right)

            while max_dq and x >= nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                # 先移左边界
                left += 1 
                if min_dq[0] < left:
                    min_dq.popleft()
                if max_dq[0] < left:
                    max_dq.popleft()

            ans = max(ans, right - left + 1)

        return ans


class Solution:
    # 只增大不减小窗口
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        left = 0

        for right, x in enumerate(nums):
            while min_dq and x <= nums[min_dq[-1]]:
                min_dq.pop()
            min_dq.append(right)

            while max_dq and x >= nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(right)

            if nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if min_dq[0] == left:
                    min_dq.popleft()
                if max_dq[0] == left:
                    max_dq.popleft()
                left += 1

        return right - left + 1