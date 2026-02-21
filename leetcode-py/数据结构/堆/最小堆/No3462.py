from typing import List
import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        sorted_grid = [sorted(row,reverse=True) for row in grid]

        # 预处理
        hq = []
        for i,limit in enumerate(limits):
            for j,n in enumerate(sorted_grid[i]):
                if j > limit -1:
                    break
                heapq.heappush(hq,-n)

        ans = 0
        for _ in range(k):
            if hq:
                ans += heapq.heappop(hq)
            else:
                break
        
        return ans
    
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        nums = []
        for row,limit in zip(grid,limits):
            row.sort(reverse = True)
            nums.extend(row[:limit])
        nums.sort(reverse = True)
        return sum(nums[:k])