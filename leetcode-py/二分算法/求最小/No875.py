from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in piles:
                count += (i - 1) // mid + 1
            if count > h:
                left = mid + 1
            else:
                right = mid
        return left # 143ms

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        if h >= total:
            return 1
        left = max(total // h , 1)
        right = max(piles) + 1
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in piles:
                count += (i - 1) // mid + 1
            if count > h:
                left = mid + 1
            else:
                right = mid
        return left # 135ms


# 这里的right还可以优化,见题解
# https://leetcode.cn/problems/koko-eating-bananas/solutions/658095/python3-yi-xing-dai-ma-you-hua-zuo-you-b-gcof/
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        mx = max(piles)
        length = len(piles)
        if h >= total:
            return 1
        if length == h:
            return mx
        left = max(total // h , 1)
        right = min(mx,(total-1)//(h-length)+1)
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in piles:
                count += (i - 1) // mid + 1
            if count > h:
                left = mid + 1
            else:
                right = mid
        return left # 12ms