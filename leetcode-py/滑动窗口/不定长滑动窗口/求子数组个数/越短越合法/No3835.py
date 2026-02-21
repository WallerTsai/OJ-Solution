
from collections import deque
from typing import List
from sortedcontainers import SortedList # type: ignore

class Solution:
    # 正难则反 + 滑动窗口 + SortedList
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sl = SortedList()
        ans = left = 0
        for i, x in enumerate(nums):
            sl.add(x)
            while (sl[-1] - sl[0]) * (i - left + 1) > k:
                sl.discard(nums[left])
                left += 1
                if left > i:
                    break
            ans += left
        return (n * (n + 1) // 2) - ans


class Solution:
    # 前置题目：No239, No2762
    # 单调队列维护 + 滑动窗口
    def countSubarrays(self, nums: List[int], k: int) -> int:
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

            while (nums[max_dq[0]] - nums[min_dq[0]]) * (right - left + 1) > k:
                left += 1
                if min_dq[0] < left:
                    min_dq.popleft()
                if max_dq[0] < left:
                    max_dq.popleft()

            ans += right - left + 1
        return ans


