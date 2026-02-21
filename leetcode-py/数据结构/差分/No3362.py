from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        hq = []
        for l, r in queries:
            heappush(hq,(r - l, l, r))

        n, m = len(nums), len(queries)
        diff = [0] * (n + 1)
        while hq:
            d, l, r = heappop(hq)
            # 思路错误

class Solution:
    # copy by 灵神
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        hq = []
        diff = [0] * (len(nums) + 1)
        cur_sumd = j = 0
        
        for i, x in enumerate(nums):
            cur_sumd += diff[i]

            while j < len(queries) and queries[j][0] <= i:
                heappush(hq,-queries[j][1])
                j += 1
            
            while cur_sumd < x and hq and -hq[0] >= i:
                cur_sumd += 1
                diff[-heappop(hq) + 1] -= 1
            
            if cur_sumd < x:
                return -1
        
        return len(hq)
