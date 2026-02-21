from heapq import heapify, heappop, heappush, heapreplace
from typing import List


class Solution:
    # 看着像是每次都选最小那两个
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)   # 建立最小堆,不用接收
        res = 0
        # 按照题目意思模拟
        while len(nums) > 1 and nums[0] < k:
            n1,n2 = heappop(nums),heappop(nums)
            heappush(nums,min(n1,n2)*2 + max(n1,n2))
            res += 1
        return res  # 305ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        while len(nums) > 1 and nums[0] < k:
            n1,n2 = heappop(nums),heappop(nums)
            heappush(nums,n1*2 + n2)
            res += 1
        return res  # 233ms

class Solution:
    # 灵神
    def minOperations(self, h: List[int], k: int) -> int:
        heapify(h)
        ans = 0
        while h[0] < k:
            x = heappop(h)
            heapreplace(h, h[0] + x * 2)
            ans += 1
        return ans  # 197ms