from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        elif total == k:
            return 1
        MIN = 1
        MAX = total // k + 1
        
        def check(i:int):
            count = 0
            for candy in candies:
                count += candy // i
            return count >= k
            
        left,right = MIN,MAX
        while left < right:
            mid = (right + left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1 # 123ms


