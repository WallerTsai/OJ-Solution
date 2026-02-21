from collections import deque
from functools import cache
from math import inf
from typing import List


class Solution:
    # 从后往前
    def minimumCoins(self, prices: List[int]) -> int:
        cnt = [0] * len(prices)
        for i in range(len(prices)-1,1,-1):
            index = min((i+1) // 2 , i-1)
            min_num,min_index = prices[i],i
            for j in range(i-1,max(index-1,-1),-1):
                if prices[j] <= min_num:
                    min_num = prices[j]
                    min_index = j
            cnt[i] = min_index
        res = 0
        for x in set(cnt):
            res += prices[x]
        return res  # 错误

# 题目有坑 第i个,下标为i-1
class Solution:
    # 递归
    def minimumCoins(self, prices: List[int]) -> int:
        length = len(prices)
        @cache
        def dfs(i:int) -> int:
            if i * 2 >= length:
                return prices[i-1]
            next_min = min(dfs(j) for j in range(i+1,i*2+2))
            return prices[i-1] + next_min
        
        return dfs(1)   # 127ms
    
class Solution:
    # 递推
    # 从后往前 
    def minimumCoins(self, prices: List[int]) -> int:
        length = len(prices)
        for i in range((length+1)//2-1,0,-1):
            prices[i-1] += min(prices[i:i*2+1])
        return prices[0]
        
class Solution:
    # 灵神
    # 单调队列优化
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque([(n + 1, 0)])  # 哨兵
        for i in range(n, 0, -1):
            while q[-1][0] > i * 2 + 1:  # 右边离开窗口
                q.pop()
            f = prices[i - 1] + q[-1][1]
            while f <= q[0][1]:
                q.popleft()
            q.appendleft((i, f))  # 左边进入窗口
        return q[0][1]



fun = Solution()
ans = fun.minimumCoins([26,18,6,12,49,7,45,45])