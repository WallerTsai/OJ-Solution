from typing import List
from collections import deque

class Solution:
    # 队列模拟
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        dq = deque(sorted(piles))
        while dq:
            dq.pop()
            dq.popleft()
            res += dq.pop()
        return res  # 81ms
    
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = cnt = 0
        piles.sort(reverse=True)
        i = 1
        while cnt < len(piles)//3:
            res += piles[i]
            cnt += 1
            i += 2
        return res  # 71ms

class Solution:
    # 列表切片
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles) // 3 :: 2]) # 68ms