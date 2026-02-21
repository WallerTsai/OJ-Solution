import heapq
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1

        ans = 0
        hq = []
        cur_sum = 1
        for n in nums:
            if n < 0:
                heapq.heappush(hq,n)
            cur_sum += n
            while cur_sum < 1:
                cur_sum += -heapq.heappop(hq)
                ans += 1
        return ans  # 39ms

fun = Solution()
fun.magicTower([100,100,100,-250,-60,-140,-50,-50,100,150])